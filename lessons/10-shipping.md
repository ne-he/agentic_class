# 10 · Shipping

## Konsep
Project yang nganggur di 90% = nilai 0. Lesson terakhir bukan teknis: **cara menutup**.
Ship dulu sebagai portfolio (jalan penuh lokal + README + demo), deploy belakangan.

## Kenapa ini lesson paling penting buatku
Pola lamaku: over-explore, under-ship — numpuk eksperimen, gak ada yang publik. Aturan baru:
tiap milestone harus *menghasilkan sesuatu yang bisa ditunjukkan*, bukan cuma "lebih rapi".

## Checklist ship (Tier A dulu)
- [ ] Tanya → jawaban + kode + chart
- [ ] Self-verify jalan, computed confidence + breakdown muncul
- [ ] 20 gold question, eval harness jalan, scorecard ada
- [ ] Docker sandbox: isolasi, limit, no network, auto-cleanup
- [ ] Verification report: Method A vs B + agreement
- [ ] README + diagram arsitektur
- [ ] Demo 2 menit + build-log post

## Urutan yang menyelamatkan
1. Risiko tertinggi duluan (sandbox), bukan yang paling enak (UI).
2. Kontrak (schema) sebelum implementasi.
3. Kalau ragu/butuh keputusan manusia → STOP & tanya, jangan nebak.
4. Fitur di luar task aktif → parkir di `IDEAS_PARKING.md`, jangan dikerjain.

## Jebakan terakhir
- **Scope creep UI** di menit akhir. UI = fase 4, bukan fase 1.
- **Deploy jadi alasan nunda ship.** Portfolio lokal yang jalan > deploy yang gak kelar.
- **Nunggu sempurna.** Selesai mengalahkan sempurna. Kirim.

## Selesai
Kembali ke [README](../README.md) · lihat implementasinya di
[agentic_analyst](https://github.com/ne-he/agentic_analyst).
