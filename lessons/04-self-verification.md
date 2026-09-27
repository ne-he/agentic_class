# 04 · Self-verification

## Konsep
Jangan percaya angka pertama. Hitung ulang **angka kunci** dengan metode kedua yang
independen, lalu bandingkan dalam toleransi:

- **Method A**: hasil agen (pandas, dieksekusi di sandbox).
- **Method B**: recompute via DuckDB SQL (in-process, deterministik).

Kalau sepakat → keyakinan naik. Kalau beda → tandai, dan angka itu **ditahan** dari ringkasan.

## Kenapa ini "verifikasi beneran"
"Minta LLM cek ulang jawabannya" bukan verifikasi, itu menebak dua kali. Verifikasi nyata =
jalur komputasi **berbeda** menghasilkan angka **sama**. Itu yang membedakan reliability
engineering dari sekadar prompt.

## Contoh
```python
def verify_numeric(dataset_id, key_value, sql, tol=1e-6):
    b = duckdb_scalar(dataset_id, sql)          # method B
    agreement, ok = compare_numbers(key_value, b, tol)
    return VerificationResult(
        method_a=f"agent: {key_value}",
        method_b=f"duckdb: {b}",
        agreement=agreement, passed=ok,
    )
```

## Tiga mekanisme (mulai dari satu)
1. **Numerical cross-check** (wajib): seperti di atas.
2. **Sanity check**: aturan domain (total revenue ≥ 0, persentase 0–100).
3. **Row-level contradiction**: minta agen cari ≤3 baris yang melawan kesimpulan.

## Jebakan
- **DuckDB ≠ pandas soal encoding/NA.** Samakan sumber data; di sini DuckDB membaca
  dataframe yang sudah dibaca pandas (encoding benar), bukan baca CSV sendiri.
- **Toleransi terlalu ketat** → false alarm pada pembulatan. Pilih toleransi relatif.

## Lanjut
→ [05 · Computed confidence](05-computed-confidence.md): ubah hasil verifikasi jadi skor.
