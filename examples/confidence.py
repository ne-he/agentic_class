"""Computed confidence (Lesson 05) — implementasi rumus tertimbang, tanpa dependency.

Jalankan:  python examples/confidence.py
"""

from __future__ import annotations

from dataclasses import dataclass

W_CONSISTENCY = 0.40
W_VERIFY = 0.30
W_TOOL = 0.20
W_COVERAGE = 0.10


@dataclass
class Confidence:
    answer_consistency: float
    verification_agreement: float
    tool_execution_success: float
    data_coverage: float

    @property
    def final(self) -> float:
        return (
            W_CONSISTENCY * self.answer_consistency
            + W_VERIFY * self.verification_agreement
            + W_TOOL * self.tool_execution_success
            + W_COVERAGE * self.data_coverage
        )

    @property
    def label(self) -> str:
        f = self.final
        return "HIGH" if f >= 0.8 else "MEDIUM" if f >= 0.5 else "LOW"


def demo() -> None:
    high = Confidence(1.0, 1.0, 1.0, 1.0)
    mixed = Confidence(0.5, 0.2, 1.0, 0.8)
    for c in (high, mixed):
        print(f"final={c.final:.2f}  label={c.label}  ({c})")

    assert high.label == "HIGH"
    assert mixed.label in ("MEDIUM", "LOW")
    print("OK — rumus konsisten.")


if __name__ == "__main__":
    demo()
