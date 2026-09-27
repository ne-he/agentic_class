# 07 · SSE streaming

## Konsep
Agen butuh waktu (beberapa detik–menit). Jangan biarkan user menatap spinner. Stream tiap
event begitu terjadi: `plan → step → tool → chart → verify → confidence → final`.
Server-Sent Events (SSE) = HTTP teks satu arah, sederhana, cocok.

## Kenapa streaming = UX + kepercayaan
Melihat "kerja"-nya (rencana, tiap tool, verifikasi) bikin user percaya prosesnya, bukan
cuma hasil. Ini sekaligus "show your work" yang jadi nilai jual.

## Contoh (format frame SSE)
```
event: verify
data: {"method_a":"agent: 286397.02","method_b":"duckdb: 286397.02","passed":true}

```
Tiap frame = `event:` + `data:` (JSON) dipisah baris kosong ganda.

## Loop sinkron → stream async
ReAct loop biasanya sinkron. Untuk streaming: jalankan loop di thread, kirim event ke
`queue.Queue`, generator async nge-yield dari queue:
```python
def worker(): result = loop.run(q, ds, on_event=events.put); events.put(SENTINEL)
# generator: baca queue → yield sse(event) sampai SENTINEL
```

## Jebakan
- **EventSource cuma GET.** `/analyze` itu POST → di klien pakai `fetch` + ReadableStream
  reader, parse frame manual.
- **Proxy yang buffer.** Beberapa proxy menahan SSE; uji end-to-end, bukan cuma lokal.
- **Simpan hasil setelah stream**, bukan sebelum: `final` event lalu `save_run`.

## Lanjut
→ [08 · Persistence](08-persistence.md): simpan tiap run biar bisa dibuka lagi.
