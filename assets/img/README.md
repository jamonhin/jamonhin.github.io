# Project images

One folder per project. Each folder has its own README with suggested filenames and,
where the project is under confidentiality, a checklist to run before committing.

| Folder | Project card | Header now |
|---|---|---|
| `nils/` | AI Document-Validation Pipeline (NILS) | amber gradient + icon |
| `sage/` | Sage — Voice AI Life-Story Platform | teal gradient + icon |
| `reporting-dashboards/` | Recruitment Reporting Warehouse & Dashboards | indigo gradient + icon |
| `awareim/` | AwareIM XML Generator | purple gradient + icon |
| `voc/` `rag/` `mortgage/` `training/` `n8n/` `deal-processing/` `cluster/` `Graph-RAG-Pr1/` `Graph-rag-Pr2/` | existing cards | real screenshots |

## Image specs

~1200×600 px (2:1), PNG or JPG, ideally under 400 KB. The card header slot is 192 px tall
(`h-48`) and roughly 560 px wide on desktop, so 2:1 crops cleanly with `object-cover`.

## Swapping a gradient placeholder for a real image

The four new cards currently render an inline gradient with a Font Awesome icon. To use an image,
replace the whole header `<div>` in `index.html`. For example, for Sage:

```html
<!-- from -->
<div class="h-48 relative bg-gray-200 flex items-center justify-center"
     style="background-image: linear-gradient(135deg, #14b8a6 0%, #047857 100%);">
    <i class="fas fa-microphone-lines text-white text-6xl opacity-90"></i>
    <div class="absolute top-0 right-0 bg-green-600 text-white px-3 py-1 m-2 rounded-full text-xs">Aug 2026 &ndash; In Progress</div>
</div>

<!-- to -->
<div class="h-48 bg-gray-200 relative">
    <img src="assets/img/sage/companion.png" alt="Sage Companion" class="w-full h-full object-cover">
    <div class="absolute top-0 right-0 bg-green-600 text-white px-3 py-1 m-2 rounded-full text-xs">Aug 2026 &ndash; In Progress</div>
</div>
```

Keep the date badge `<div>` exactly as it is — only the background and icon change.

## A note on Tailwind

`index.html` loads **precompiled Tailwind 2.2.19**, whose palette has no `teal`, `emerald`,
`amber`, `orange`, `cyan`, `sky`, `rose`, `lime`, `violet`, `slate`, `zinc`, `neutral`, `stone`
or `fuchsia` (all verified against the actual CDN file). Only `gray`, `red`, `yellow`, `green`,
`blue`, `indigo`, `purple` and `pink` work as utility classes. That is why the
new headers use inline `linear-gradient` instead of `from-*`/`to-*` classes. If you add gradient
classes from a Tailwind 3 palette they will silently render as no background at all.

## Carousels

Cards with 3+ images use a carousel (see `voc/`, `rag/`, `deal-processing/`). The wiring lives at
the bottom of `index.html` — each carousel needs a unique `id` on the header div and a matching
`initCarousel('<id>')` call. Drop the images in and ask me to convert the card; I'll wire it up.
