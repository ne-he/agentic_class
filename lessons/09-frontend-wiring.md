# 09 · Frontend wiring

## Konsep
Satu sumber kebenaran untuk tipe data: definisikan schema (Pydantic) **sekali** di backend,
mirror ke `types.ts` di frontend. Event SSE & response API pakai bentuk yang sama persis.

## Kenapa satu kontrak
Saat FE dan BE punya definisi tipe sendiri-sendiri, mereka pelan-pelan menyimpang dan UI
nampilin field yang sudah berubah. Satu kontrak (di-export jadi JSON schema) = sambungan
design ↔ API yang tak pecah.

## Contoh (mirror tipe)
```python
# backend: core/schemas.py
class ConfidenceBreakdown(BaseModel):
    answer_consistency: float; verification_agreement: float
    tool_execution_success: float; data_coverage: float
    final: float; label: Literal["HIGH","MEDIUM","LOW"]
```
```ts
// frontend: lib/types.ts (mirror)
export interface ConfidenceBreakdown {
  answer_consistency: number; verification_agreement: number;
  tool_execution_success: number; data_coverage: number;
  final: number; label: "HIGH" | "MEDIUM" | "LOW";
}
```

## Klien SSE di browser
```ts
const res = await fetch(`${API}/analyze`, { method: "POST", body: JSON.stringify(req) });
const reader = res.body!.getReader();
// decode → pisah "\n\n" → parse tiap frame → onEvent(ev)
```

## Jebakan
- **CORS.** Browser → backend butuh `CORSMiddleware`; izinkan origin frontend.
- **UI sebelum engine.** Bangun fungsi (sandbox+verify+eval) dulu; UI itu fase terakhir.
- **Mock data ketinggalan.** Ganti SEMUA mock dengan data real dari endpoint.

## Lanjut
→ [10 · Shipping](10-shipping.md): cara menutup, bukan menambah.
