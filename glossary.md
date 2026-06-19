# Glosarium

**Agent** — model + tools + loop + guardrail. Yang membuat "agentic" adalah loop
reason→act→observe, bukan modelnya.

**ReAct** — pola *Reason + Act*: model bergantian berpikir dan memanggil tool, melihat
hasil, lalu memutuskan langkah berikut.

**Tool** — fungsi yang bisa dipanggil agen, berkontrak (`name`, `description`, `parameters`).

**Sandbox** — lingkungan tereisolasi (Docker) tempat kode buatan LLM dieksekusi: tanpa
jaringan, batas CPU/memori/waktu, non-root, auto-cleanup.

**Self-verification** — menghitung ulang angka kunci dengan metode independen lalu
membandingkan dalam toleransi. *Bukan* "minta LLM cek ulang".

**Method A / Method B** — dua jalur komputasi berbeda untuk angka yang sama (mis. pandas vs
DuckDB SQL). Sepakat → keyakinan naik.

**Computed confidence** — skor keyakinan yang *dihitung* dari sinyal terukur, bukan ditebak
LLM. Bisa diaudit per komponen.

**Hallucination flag** — penanda "yakin tapi salah": confidence HIGH/MEDIUM tapi jawaban salah.

**Gold set** — kumpulan pertanyaan + jawaban benar terverifikasi manual; tolok ukur eval.

**Graded correctness** — 1.0 (tepat) / 0.5 (approach benar, angka meleset) / 0.0 (salah).

**SSE** — Server-Sent Events: stream teks satu arah HTTP untuk menampilkan event real-time.

**Reproducible bundle** — paket hasil lengkap (jawaban + kode + chart + verifikasi +
confidence + hash dataset) sehingga run bisa diulang dan menghasilkan hal sama.

**Time-to-insight** — durasi dari pertanyaan masuk sampai jawaban final.
