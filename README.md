# agentic-class — Building Verified Agentic Systems

Catatan belajar + mini-kurikulum yang aku susun sambil ngebangun
[**ANALYST — Verified Analytics Agent**](https://github.com/ne-he/agentic_analyst):
agen data analyst yang nulis kodenya sendiri, jalanin di sandbox, dan **memverifikasi tiap angka**.

Repo ini fokus ke *kenapa* dan *bagaimana* — bukan sekadar kode jadi, tapi keputusan
engineering di baliknya. Ditulis biar bisa aku baca ulang 6 bulan lagi (dan dipahami orang lain).

## Kurikulum

| # | Topik | Inti |
|---|---|---|
| 00 | [Apa itu "agent" sebenarnya](lessons/00-what-is-an-agent.md) | Loop, bukan model |
| 01 | [ReAct loop](lessons/01-react-loop.md) | Reason → Act → Observe |
| 02 | [Docker sandbox](lessons/02-docker-sandbox.md) | Jalanin kode LLM dengan aman |
| 03 | [Desain tool](lessons/03-tool-design.md) | Kontrak yang dipahami LLM |
| 04 | [Self-verification](lessons/04-self-verification.md) | Hitung ulang, jangan percaya |
| 05 | [Computed confidence](lessons/05-computed-confidence.md) | Skor yang dihitung, bukan ditebak |
| 06 | [Eval harness](lessons/06-eval-harness.md) | Nilai agen vs gold set |
| 07 | [SSE streaming](lessons/07-sse-streaming.md) | Tampilkan "kerja"-nya real-time |
| 08 | [Persistence](lessons/08-persistence.md) | Simpan tiap run, portable |
| 09 | [Frontend wiring](lessons/09-frontend-wiring.md) | Satu kontrak FE↔BE |
| 10 | [Shipping checklist](lessons/10-shipping.md) | Selesai > sempurna |

## Cara pakai
Baca berurutan. Tiap lesson punya bagian **Konsep → Kenapa → Contoh → Jebakan**.
Contoh kode ada di [`examples/`](examples/), latihan di [`exercises.md`](exercises.md).

> Prinsip pegangan: *"An analyst that writes its own code, checks its own math,
> and grades its own homework."*
