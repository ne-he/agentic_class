# 05 · Computed confidence

## Konsep
Confidence **dihitung dari sinyal**, bukan diminta ke LLM ("seberapa yakin kamu?").
Rumus tertimbang:

```
final = 0.40·answer_consistency
      + 0.30·verification_agreement
      + 0.20·tool_execution_success
      + 0.10·data_coverage
→ HIGH (≥0.8) / MEDIUM (≥0.5) / LOW (<0.5)
```

Tiap komponen punya makna dan bisa dijelaskan — bukan angka ajaib.

## Kenapa dihitung, bukan ditebak
"LLM bilang high" tak terkalibrasi: model bisa pede tapi salah. Skor terhitung bisa
**diaudit**: kalau LOW, kamu bisa tunjuk komponen mana yang menyeretnya turun. Ini bahasa
yang dimengerti stakeholder.

## Contoh
```python
W = dict(consistency=.40, verify=.30, tool=.20, coverage=.10)
final = (W["consistency"]*answer_consistency
       + W["verify"]*verification_agreement
       + W["tool"]*tool_execution_success
       + W["coverage"]*data_coverage)
label = "HIGH" if final>=.8 else "MEDIUM" if final>=.5 else "LOW"
```

## Mendefinisikan komponen
- **answer_consistency** — 1.0 dikurangi penalti per kontradiksi yang ditemukan.
- **verification_agreement** — agreement Method A vs B (0–1); netral 0.5 bila tak ada cek.
- **tool_execution_success** — rasio tool call sukses.
- **data_coverage** — proporsi data relevan yang benar-benar tersentuh.

## Jebakan
- **Bobot asal.** Tulis alasan tiap bobot; konsistensi jawaban paling berat (0.40) karena
  paling sering jadi sumber error.
- **Selalu 1.0.** Kalau skor tak pernah turun, sinyalnya kurang tajam — uji dengan kasus salah.

## Lanjut
→ [06 · Eval harness](06-eval-harness.md): ukur apakah confidence ini benar berkorelasi.
