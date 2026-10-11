# James Montoya — Resume

Single-source resume in HTML, built for screen reading and for printing to PDF.

## Files

- `james-montoya-resume.html` — the resume. This is the only source; edit it here.
- `generate_pdf.py` — optional script for automated PDF generation
- `README.md` — this file

> There used to be a second file, `james-montoya-resume-pdf.html`. It drifted out of sync
> with this one — different summary, different role list, different claimed years of
> experience — and both were linked publicly from the portfolio. It has been removed.
> Keep one source.

## Generating a PDF

### From the browser (recommended)
1. Open `james-montoya-resume.html`
2. Click **📄 Save as PDF** (top right) — this opens the print dialog
3. Choose "Save as PDF" as the destination, set margins to minimum
4. Save as `James-Montoya-Resume.pdf`

### From the command line
```bash
pip install weasyprint
python3 generate_pdf.py
```

## Keeping it consistent with the portfolio

These must match `index.html`, or the site contradicts itself:

| | Value |
|---|---|
| Headline | AI Engineer — Document AI, RAG Systems & Agentic Pipelines |
| Experience framing | Twenty years' career, twelve of them in enterprise data engineering |
| Email | james@ethicalaispecialists.com.au |
| LinkedIn | linkedin.com/in/james-montoya |
| Portfolio | jamonhin.github.io |

## Confidentiality

The not-for-profit client behind the DocTriage work is **not named** here, matching how the
portfolio and the project page describe them ("an Australian no-interest loan (NILS)
provider" / "an Australian Not-for-Profit"). Do not add the client's name without written
permission — this file is published publicly at
`jamonhin.github.io/assets/resume/james-montoya-resume.html`.

---

*Last updated: October 2026*
