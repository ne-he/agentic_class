# Latihan

Kerjakan setelah baca lesson terkait. Tujuannya paham *kenapa*, bukan hafal kode.

## L01 — ReAct loop
1. Di [`examples/react_loop_minimal.py`](examples/react_loop_minimal.py), tambahkan tool
   `count_loss_rows` (hitung baris profit < 0). Pandu LLM-script memakainya.
2. Buat `generate` yang sengaja balas non-JSON di langkah pertama. Pastikan loop tidak crash.

## L02 — Sandbox
3. Tulis daftar 5 hal berbahaya yang bisa dilakukan kode tak ter-sandbox pada CSV/host.
   Untuk tiap satu, batasan sandbox mana yang menutupnya?

## L04 — Self-verification
4. Di [`examples/cross_check.py`](examples/cross_check.py), ubah `tol` jadi `0.2` (20%).
   Apakah kasus "meleset" sekarang lolos? Apa risikonya toleransi kelonggaran?

## L05 — Confidence
5. Cari kombinasi komponen yang menghasilkan label **LOW** walau `tool_execution_success=1.0`.
   Komponen mana paling "berkuasa" menurunkan skor, dan kenapa bobotnya segitu?

## L06 — Eval
6. Tulis 3 gold question untuk dataset pilihanmu: satu descriptive, satu statistical,
   satu **edge-case jebakan** (jawaban benar = "data tak tersedia"). Sertakan `expected_value`
   dan `allowed_tolerance`.

## L10 — Shipping
7. Ambil satu project lamamu yang mangkrak. Tulis checklist 5 item paling kecil untuk
   membawanya ke "bisa ditunjukkan". Kerjakan item pertama hari ini.
