"""Numerical cross-check (Lesson 04): bandingkan dua metode dalam toleransi.

Method A = "hasil agen", Method B = "recompute independen". Tanpa dependency.

Jalankan:  python examples/cross_check.py
"""

from __future__ import annotations


def compare_numbers(a: float, b: float, tol: float = 1e-6) -> tuple[float, bool]:
    """Kembalikan (agreement 0..1, within_tolerance)."""
    if a == b:
        return 1.0, True
    denom = max(abs(a), abs(b), 1e-9)
    rel_diff = abs(a - b) / denom
    agreement = max(0.0, 1.0 - rel_diff)
    return agreement, rel_diff <= tol


def verify(key_value: float, recomputed: float, tol: float = 1e-6) -> dict:
    agreement, ok = compare_numbers(key_value, recomputed, tol)
    return {
        "method_a": f"agent: {key_value}",
        "method_b": f"recompute: {recomputed}",
        "agreement": round(agreement, 4),
        "passed": ok,
    }


if __name__ == "__main__":
    # Kasus cocok → passed True, agreement 1.0
    ok = verify(286397.02, 286397.02)
    print("cocok    :", ok)
    assert ok["passed"] and ok["agreement"] == 1.0

    # Kasus meleset → passed False, agreement < 1.0
    bad = verify(286397.02, 250000.0)
    print("meleset  :", bad)
    assert not bad["passed"] and bad["agreement"] < 1.0

    print("OK: cross-check menangkap selisih.")
