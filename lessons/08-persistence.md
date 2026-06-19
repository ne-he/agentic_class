# 08 · Persistence

## Konsep
Tiap run disimpan: `run_history`, `scorecards`, `gold_questions`, `artifacts`. Pakai
SQLite via SQLAlchemy 2.0 — gratis, tanpa akun, tapi **portable** ke Postgres (Neon) nanti
cukup ganti connection string.

## Kenapa SQLite dulu
MVP tak butuh DB hosted. SQLite = satu file, nol setup, cukup buat ribuan run. Yang penting:
**jangan tulis query SQLite-only** supaya migrasi ke Postgres mulus.

## Contoh (ORM portable)
```python
class RunHistory(Base):
    __tablename__ = "run_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    question: Mapped[str] = mapped_column(Text)
    answer_markdown: Mapped[str] = mapped_column(Text)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
```

## Satu jebakan path yang mahal
`DATABASE_URL=sqlite:///./backend/analyst.db` itu **relatif ke CWD**. Jalankan server dari
folder berbeda → "unable to open database file". Solusi: normalisasi path SQLite relatif ke
root project, dan pastikan folder induknya ada. Bug ini lolos dari unit test (pakai DB
sementara absolut) — ketahuan baru saat smoke-test server sungguhan.

## Jebakan lain
- **`datetime.utcnow` deprecated** → pakai timezone-aware `datetime.now(timezone.utc)`.
- **Session bocor.** Pakai context manager; commit/rollback/close yang rapi.

## Lanjut
→ [09 · Frontend wiring](09-frontend-wiring.md): satu kontrak biar FE & BE tak pernah beda.
