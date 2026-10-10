# NILS — AI Document-Validation Pipeline · Screenshots

Card in `index.html`: *"AI Document-Validation Pipeline for No-Interest Microloan Assessments"*.
Currently uses an amber gradient + `fa-file-contract` placeholder.

## ⚠️ CONFIDENTIAL — read before adding anything here

This is a client engagement under confidentiality. Anything committed here is **public on GitHub Pages**.

Every image must be checked for:

- [ ] **No client name, logo or branding** anywhere in the frame (window title, header, footer, favicon, URL bar).
- [ ] **No real applicant data** — no names, addresses, CRN, Medicare, licence or bank-account numbers. Synthetic applicants only.
- [ ] **No specific business rules or thresholds** — no default amounts, freshness windows or per-category caps visible in decision tables or rule output.
- [ ] **No infrastructure detail** — no IPs, hostnames, ports, container names, file paths, API keys or credentials.
- [ ] **No internal identifiers** — no Drive folder IDs, n8n workflow IDs or CRM org details.
- [ ] **No client staff names** in comments, assignees or audit trails.

If in doubt, blur it or don't commit it. Prefer purpose-built synthetic demos over real screens.

## Suggested filenames

- `pipeline.png` — architecture diagram (safest option: no live data at all)
- `extraction.png` — field extraction with confidence flags, **synthetic applicant**
- `decision-tables.png` — rules engine structure with **rule values redacted**
- `triage.png` — triage recommendation with cited reasons, **synthetic applicant**

A redacted architecture diagram is the lowest-risk and usually the most impressive choice here.

## Image specs

~1200×600 px (2:1), PNG or JPG, ideally under 400 KB. The card header slot is 192 px tall and roughly 560 px wide on desktop.

---

## Estado actual (9 Oct 2026)

Las cuatro están en un **carrusel** en la tarjeta (`id="nils-carousel"`), en este orden:

| # | Archivo | Origen | Redacción aplicada |
|---|---|---|---|
| 1 | `triage.png` | `review_results.png` | umbrales de elegibilidad |
| 2 | `pipeline.png` | `n8n_pipeline_APIs.png` | hostname, puerto, nombres de credencial |
| 3 | `pipeline-ingest.png` | `n8n_pipeline_collect_docs.png` | ruta con usuario, ID de workflow |
| 4 | `documents.png` | `drive_view.png` | ninguna — solicitante sintético |

Todas reescaladas a 1600 px y optimizadas (~1,5 MB en total).

### Detalle de lo redactado

**`triage.png`** — se taparon, con el color de fondo de cada tarjeta, los valores que el
punto 3 del brief clasifica como política del cliente: `(min. 2 forms)`,
`3 forms of ID provided — current, addresses match`, `Verify: Currency (≤14 days)`,
`(90 days)` en Bank statements, y los criterios del informe crediticio.
Se conservó el banner **SYSTEM RECOMMENDATION: PROCEED — «Automated recommendation only…
The final decision is yours»**, que es la prueba visual del principio human-in-the-loop.

**`pipeline.png`** — `http://nils-review:8000/api/runs`, el aviso con `x-api-key` /
`REVIEW_INGEST_KEY`, y la etiqueta `POST http://nils-review:8000…` del nodo de ingest.

**`pipeline-ingest.png`** — `cd /home/jamesm/ocr-verify && OCRV_VENV=… ./run.sh`
(ruta con nombre de usuario) y `Workflow: onmJ3qg00UmaH…` (ID interno de n8n).

**`documents.png`** — sin redactar. Los documentos son dummies: el solicitante es «Peter Pan» y los valores (Medicare, CRN, fecha de nacimiento, domicilio, licencia) son sintéticos, generados para pruebas. No hay PII real que proteger. Los nombres de archivo muestran además la taxonomía documental que procesa el pipeline.

Se conservaron a propósito las notas que documentan el diseño orientado a privacidad
(«el nombre del cliente nunca sale de aquí», `case_ref` como seudónimo, el bloque
«Anonymized twin → corpus»): son el mejor argumento técnico de la pieza.

### Pendiente de criterio

En `triage.png`, el panel inferior derecho conserva *«System finding: no defaults, no
debt-collector accounts, no public records, no recent arrears»*. No es un umbral numérico
sino un hallazgo sobre un solicitante sintético, con lenguaje estándar del sector, así que
se dejó visible. Si lo consideras política del cliente, se tapa igual que el resto.

Nota: la redacción de `triage.png` responde al punto 3 del brief (reglas y umbrales del
cliente), no al punto 5 (PII). Que los solicitantes sean sintéticos no cambia ese punto —
`≤14 days` o `min. 2 forms` siguen siendo la política del cliente, no datos del solicitante.

### Si reemplazas alguna imagen

Volver a aplicar la redacción sobre la captura nueva — los originales sin redactar
**no** deben copiarse a esta carpeta.
