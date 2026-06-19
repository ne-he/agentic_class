# 03 · Desain tool

## Konsep
Tool = fungsi yang bisa dipanggil agen, dibungkus kontrak yang **LLM bisa baca**:
`name`, `description`, `parameters` (JSON schema). MVP cukup 3–4 tool yang tajam:

- `inspect_schema(dataset_id)` → kolom, tipe, 5 baris sampel (via DuckDB).
- `write_and_execute(code)` → jalankan pandas di sandbox, balikin stdout.
- `make_chart(code)` → eksekusi di sandbox, balikin path PNG.

## Kenapa sedikit tool itu bagus
Tiap tool = ruang keputusan tambahan buat model. Kebanyakan tool → model bingung, tool
salah-pakai. 3 tool yang jelas mengalahkan 12 tool yang tumpang-tindih. Tambah tool hanya
kalau ada pertanyaan yang benar-benar tak terjawab tanpa itu.

## Contoh (kontrak tool)
```python
class Tool(ABC):
    name: str
    description: str
    parameters: dict           # JSON schema -> diberikan ke LLM
    def run(self, *, dataset_id: str, **kwargs) -> ToolRunResult: ...
```
Registry sederhana keyed by `name`; agen memilih lewat string `action`.

## Jebakan
- **Deskripsi kabur** → model salah pilih. Tulis seakan untuk junior dev.
- **Tool yang diam-diam punya efek samping** (nulis file, network). Tetap lewat sandbox.
- **Output tool kepanjangan** → boros token. Ringkas/truncate observasi.

## Lanjut
→ [04 · Self-verification](04-self-verification.md): setelah agen jawab, buktikan angkanya.
