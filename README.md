# buildingyourown.ai

Landing site for the Build Days: one-day, hands-on AI build workshops for innovators in small and mid-sized companies. Static HTML + CSS, no build step, GitHub Pages.

- `index.html` — the one page.
- `assets/site.css` — the family token block (between the `shared tokens` markers, synced from the family design tokens; do not edit there) plus this site's own layout below it.
- `assets/*.webp` — illustrations, image prompts and catalog are kept with the content source, outside this repo.

## Go-live checklist
1. DNS at Dynadot: mode "Dynadot DNS" (not parking), apex A-records 185.199.108.153 / .109.153 / .110.153 / .111.153, `www` CNAME → `jacovanderlaan.github.io`. Check: `nslookup buildingyourown.ai 8.8.8.8`.
2. GitHub Pages: custom domain green, then enforce HTTPS.
3. Remove the `TESTPHASE-NOINDEX` meta line in `index.html` and replace `robots.txt` with `robots.txt.golive`.
4. Replace the LinkedIn call-to-action with the questionnaire link once the form exists; add the privacy statement page.
