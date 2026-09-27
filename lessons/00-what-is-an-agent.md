# 00 · Apa itu "agent" sebenarnya

## Konsep
"Agent" bukan model yang lebih pintar. Agent = **loop** di sekeliling model:

```
while belum_selesai:
    pikiran, aksi = model(konteks)      # reason
    hasil = jalankan(aksi)              # act
    konteks += hasil                    # observe
```

Modelnya tetap LLM biasa. Yang bikin "agentic" adalah: ia boleh **memilih tindakan**,
**melihat hasilnya**, lalu **memutuskan langkah berikut**, berulang sampai cukup bukti.

## Kenapa ini penting
"Chat with CSV" = satu panggilan model → jawaban. Tidak ada eksekusi, tidak ada
verifikasi, tidak ada jejak. Agent = model + tools + loop + guardrail. Bedanya:
agent bisa **menghitung beneran** (lewat tool), bukan menebak angka dari teks.

## Contoh
Pertanyaan: *"Region mana yang profitnya paling rendah?"*
- Tebakan model murni → bisa halusinasi angka.
- Agent → `inspect_schema` (lihat kolom) → `write_and_execute` (groupby+sum di sandbox)
  → baca hasil → jawab dengan angka yang benar-benar dihitung.

## Jebakan
- **Loop tak berbatas.** Wajib ada `max_tool_calls` + budget token, kalau tidak bisa muter selamanya.
- **Model "ngarang tool".** Validasi nama tool; tolak yang tak terdaftar.
- **Mengira lebih banyak langkah = lebih pintar.** Sering kebalikannya; ukur efisiensi tool.

## Lanjut
→ [01 · ReAct loop](01-react-loop.md): protokol konkret buat loop ini.
