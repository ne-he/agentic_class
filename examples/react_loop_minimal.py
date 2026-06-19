"""ReAct loop minimal — tanpa LLM/Docker, biar konsepnya kelihatan telanjang.

`generate` di-inject (di sini fungsi palsu yang di-script). Ini pola yang sama dipakai
di project asli supaya loop bisa diuji tanpa kuota API.

Jalankan:  python examples/react_loop_minimal.py
"""

from __future__ import annotations

import json
from typing import Callable

GenerateFn = Callable[[str], str]

# "Dataset" kecil di memori biar contoh self-contained.
ROWS = [
    {"region": "West", "profit": 100},
    {"region": "East", "profit": 60},
    {"region": "West", "profit": 50},
    {"region": "Central", "profit": -20},
]

# Tools sederhana ------------------------------------------------------------

def tool_inspect_schema() -> str:
    cols = sorted({k for r in ROWS for k in r})
    return f"columns={cols} n_rows={len(ROWS)} sample={ROWS[:2]}"


def tool_sum_profit_by_region() -> str:
    agg: dict[str, float] = {}
    for r in ROWS:
        agg[r["region"]] = agg.get(r["region"], 0) + r["profit"]
    return json.dumps(agg)


TOOLS = {"inspect_schema": tool_inspect_schema, "sum_profit": tool_sum_profit_by_region}


def react(question: str, generate: GenerateFn, max_steps: int = 6) -> dict:
    transcript = f"Pertanyaan: {question}\n"
    for _ in range(max_steps):
        raw = generate(transcript)
        action = json.loads(raw)
        if "final" in action:
            return action
        name = action.get("action")
        if name not in TOOLS:
            transcript += f"[Observasi] tool '{name}' tak ada\n"
            continue
        obs = TOOLS[name]()
        transcript += f"[Aksi] {name}\n[Observasi] {obs}\n"
    return {"final": "berhenti: batas langkah", "code": ""}


def scripted_llm() -> GenerateFn:
    """LLM palsu: lihat skema → hitung → jawab region dengan profit tertinggi."""
    steps = [
        {"thought": "lihat data", "action": "inspect_schema", "args": {}},
        {"thought": "agregasi", "action": "sum_profit", "args": {}},
        {"final": "Region profit tertinggi = **West (150)**", "code": "groupby+sum",
         "key_value": 150},
    ]
    it = iter(steps)
    return lambda _prompt: json.dumps(next(it))


if __name__ == "__main__":
    result = react("Region mana profit tertinggi?", scripted_llm())
    print("JAWABAN:", result["final"])
    assert result.get("key_value") == 150, "harusnya West=150"
    print("OK — loop selesai, angka cocok.")
