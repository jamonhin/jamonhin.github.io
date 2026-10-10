# Recruitment Reporting Warehouse & Executive Dashboards · Screenshots

Card in `index.html`: *"Recruitment Reporting Warehouse & Executive Dashboards"*.
Currently uses an indigo/blue gradient + `fa-chart-line` placeholder.

> **Folder name is deliberately generic.** The client is anonymised throughout the portfolio as
> *"a Defence & Government recruitment firm"* — matching how `index.html` already described them
> before these cards existed. Folder paths are visible in the public repo, so the client name is
> not used here either. Don't rename this folder to the client's name without their written sign-off.

## ⚠️ CONFIDENTIAL — read before adding anything here

Anything committed here is **public on GitHub Pages**.

- [ ] **No client name, logo or branding** — check Grafana dashboard titles, org name, nav bar and browser tab.
- [ ] **No real candidate or client-contact data** — no names, emails, phone numbers or CRM record IDs.
- [ ] **No real revenue or commercial figures** — these are the client's commercially sensitive numbers.
- [ ] **No security-clearance data tied to identifiable people.**
- [ ] **No infrastructure** — no hostnames, IPs, ports, database names, container names or connection strings.
- [ ] **No CRM org details or internal workflow IDs.**

Grafana screenshots leak a lot by default (org name in the top bar, panel titles, real values in
tooltips and legends). Either anonymise the data source first or show the architecture instead.

## Suggested filenames

- `architecture.png` — HubSpot → n8n → ArangoDB → query API → Grafana flow (**lowest risk, recommended**)
- `master-report.png` — operational dashboard with **axis values and legends anonymised**
- `loss-analysis.png` — revenue dashboard with **figures replaced by synthetic values**
- `warehouse-model.png` — data model / collection structure

## Image specs

~1200×600 px (2:1), PNG or JPG, ideally under 400 KB. The card header slot is 192 px tall and roughly 560 px wide on desktop.
