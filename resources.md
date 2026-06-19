# Sumber & rujukan

Bacaan yang membentuk materi ini. Bukan daftar lengkap — yang benar-benar kepakai.

## Pola agen
- **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao dkk., 2022) — dasar
  loop reason→act→observe.
- Dokumentasi function-calling / structured output Gemini & pola tool-use pada umumnya.

## Eksekusi & isolasi
- Docker SDK for Python — `containers.run` dengan `network_disabled`, `mem_limit`, `pids_limit`.
- Prinsip least-privilege: user non-root, filesystem read-only untuk dataset.

## Data engine
- **DuckDB** — analitik in-process, baca CSV langsung, cocok untuk recompute verifikasi.

## Backend
- **FastAPI** + Server-Sent Events untuk streaming.
- **SQLAlchemy 2.0** (gaya `Mapped`/`mapped_column`) — ORM portable SQLite → Postgres.

## Frontend
- **Next.js 14** App Router + Tailwind. Mirror tipe dari schema backend.

## Evaluasi
- Ide eval LLM: graded correctness, LLM-as-judge, kategorisasi kegagalan.

## Implementasi rujukan
- [github.com/ne-he/agentic_analyst](https://github.com/ne-he/agentic_analyst) — semua konsep
  di repo ini diterapkan utuh di sana.
