# NILS / DocTriage — Screenshots

Images used by the DocTriage card in `index.html` and by `projects/doctriage.html`.

## ⚠️ This folder is published

Everything here is served publicly at `jamonhin.github.io/assets/img/nils/`, **including this
file**. Describe redactions by category only. Never write the redacted value down here — that
would defeat the point of removing it from the image.

## Before adding or replacing any image

Check every frame for:

- [ ] **Client identity** — name, logo, branding, account avatar, or an application header
      carrying the client's name. Anywhere on screen, including browser chrome.
- [ ] **Eligibility rules and thresholds** — anything stating a required count, a freshness
      window, or a per-category cap. These are the client's policy, not your work.
- [ ] **Infrastructure** — hostnames, ports, URLs, container or service names, filesystem paths
      (which usually carry a username), environment-variable names, credential names.
- [ ] **Internal identifiers** — workflow ids, execution ids, Drive folder ids, CRM org details.
- [ ] **Applicant data** — synthetic applicants only. The current set uses obviously fictional
      names, which is deliberate: a viewer can tell at a glance that nothing is real.
- [ ] **Browser and desktop chrome** — open tabs, bookmarks bar, address bar, notification
      counts, dock icons.

If in doubt, crop it out. An architecture diagram with no live data is almost always the
stronger portfolio image anyway.

## Current set

| File | Shows | Redaction applied |
|---|---|---|
| `triage.png` | Review console with the system's recommendation | Policy threshold values masked with each card's own background colour |
| `pipeline.png` | Document-processing sub-workflow | Service endpoint and credential-name callouts boxed out |
| `pipeline-ingest.png` | Ingestion orchestration and OCR health gate | Shell path and workflow id boxed out |
| `documents.png` | An applicant's document pack | None needed — the applicant is synthetic |

All four are capped at 1600px wide and optimised to stay under ~450KB.

What was deliberately **kept** matters as much as what was removed: the notes documenting
pseudonymous case references, the masked-by-default identifiers, and the "anonymised twin"
step are the strongest technical argument in the set.

## Image specs

~1200×600 (2:1), PNG or JPG, under 400KB. The card header slot is 192px tall and roughly 560px
wide on desktop, so 2:1 crops cleanly under `object-cover`. The detail page shows the same
images at `h-64 md:h-96`.

## If you replace an image

Re-apply the redaction to the new capture before it enters this folder. Do not stage an
unredacted original here "temporarily" — it would be committed, and git history is public.
