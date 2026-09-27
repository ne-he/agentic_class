# 06 · Eval harness

## Konsep
Tanpa pengukuran, "agennya bagus" cuma perasaan. Eval harness menilai tiap run terhadap
**gold set** (pertanyaan + jawaban benar yang sudah diverifikasi manual):

- **Correctness** (graded): 1.0 (tepat), 0.5 (approach benar angka meleset), 0.0 (salah).
- **Cost**: token in+out × harga.
- **Tool efficiency**: makin sedikit tool call untuk jawaban benar makin bagus.
- **Time-to-insight**: durasi pertanyaan → jawaban final.
- **Hallucination flag**: confident tapi salah.
- **Verification accuracy**: dari kasus salah, berapa % ditangkap verifikasi.

## Kenapa ini "naik kelas"
Gold set = 40% nilai project dan **tak bisa diotomatisasi**: kalau gold-nya salah, seluruh
eval bohong. Ini kerja manual yang mengubah tutorial jadi engineering. Eval = bukti kamu
paham ML observability.

## Contoh (grading numerik)
```python
def numeric_correctness(answer, expected, tol):
    got = extract_first_number(answer)
    if got is None: return None                  # fallback ke LLM-judge
    rel = abs(got - expected) / abs(expected or 1)
    return 1.0 if rel <= tol else 0.5 if rel <= tol*5 else 0.0
```

## Hallucination flag (yang bikin beda)
```python
flag = correctness < 0.5 and confidence.label in ("HIGH", "MEDIUM")
```
"Yakin tapi salah" justru yang paling berbahaya, itu yang harus ketangkep.

## Jebakan
- **Gold set kekecilan/seragam.** Campur descriptive/diagnostic/predictive/statistical/edge.
- **Edge case "jebakan"** (tanya tahun yang datanya tak ada) menguji kejujuran agen.

## Lanjut
→ [07 · SSE streaming](07-sse-streaming.md): tampilkan semua ini bergerak real-time.
