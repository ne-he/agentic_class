# 02 · Docker sandbox

## Konsep
Kode yang ditulis LLM **tidak boleh** jalan di proses backend utama. Ia jalan di
container Docker sekali-pakai: tanpa jaringan, batas CPU/memori/waktu, user non-root,
hanya library yang di-whitelist, lalu container dihapus.

## Kenapa ini pilar #1
Ini pembeda paling tegas dari "wrapper LLM". `exec()` kode model di server = lubang
keamanan fatal (baca file, kirim data keluar, infinite loop). Sandbox = bukti kamu paham
**security & systems**, bukan cuma manggil API.

## Contoh (batasan saat run)
```python
container = client.containers.run(
    image="analyst-sandbox:latest",
    command=["python", "/work/run.py"],
    network_disabled=True,          # no network
    mem_limit="512m",
    nano_cpus=2_000_000_000,         # 2 CPU
    pids_limit=128,
    volumes={dataset: {"bind": "/data/dataset.csv", "mode": "ro"}},  # read-only
    detach=True,
)
container.wait(timeout=30)           # anti-hang
```

## Aturan keras
1. **HANYA** kode LLM yang lewat sandbox. `exec`/`eval` di backend = haram.
2. Verifikasi (SQL deterministik via DuckDB) boleh in-process — itu *bukan* kode LLM.
3. Selalu auto-cleanup; pindahkan artefak (PNG chart) keluar sebelum container dihapus.

## Jebakan
- **Timeout Windows named pipe**: `container.wait` bisa lempar `ConnectionError`, bukan
  cuma `ReadTimeout`. Tangkap keduanya.
- **Fallback dev**: sediakan mode subprocess (`USE_DOCKER=false`) biar cepat saat ngoprek,
  tapi target portfolio tetap Docker.

## Lanjut
→ [03 · Desain tool](03-tool-design.md): bagaimana agen "memanggil" sandbox ini.
