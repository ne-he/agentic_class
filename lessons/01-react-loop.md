# 01 · ReAct loop

## Konsep
ReAct = **Reason + Act**. Tiap giliran, model membalas **satu objek JSON**, salah satu dari:

```json
{ "thought": "alasan singkat", "action": "nama_tool", "args": { } }
```
atau, kalau sudah cukup bukti:
```json
{ "final": "jawaban markdown", "code": "kode kunci", "key_value": 286397.02,
  "verify_sql": "SELECT SUM(\"Profit\") FROM t" }
```

Loop-nya: kirim transcript → parse JSON → kalau `action` jalankan tool & tambah observasi
ke transcript → ulang. Kalau `final`, selesai.

## Kenapa protokol JSON custom (bukan native function-calling)
- **Robust**: gampang di-parse, gampang kasih fallback kalau model balas non-JSON.
- **Testable**: `generate` bisa di-*inject* dengan fungsi palsu → uji loop tanpa kuota API.
- **Transparan**: tiap langkah kelihatan, enak buat "show your work" di UI.

## Contoh (inti loop)
```python
for _ in range(max_tool_calls):
    raw = generate(transcript + "\nBalas JSON:")
    action = json.loads(strip_fences(raw))
    if action.get("final"):
        return finish(action)
    tool = registry.get(action["action"])
    obs = tool.run(**action.get("args", {}))
    transcript += f"\n[Observasi] {obs}\n"
```

## Jebakan
- **Code fence.** Model sering bungkus JSON dengan ```` ```json ````; strip dulu.
- **Non-JSON.** Jangan crash: balas "format salah, ulangi" lalu lanjut.
- **Transcript membengkak.** Hitung perkiraan token; stop kalau lewat budget.

## Lanjut
→ [02 · Docker sandbox](02-docker-sandbox.md): di mana `tool.run()` untuk kode LLM dieksekusi.
