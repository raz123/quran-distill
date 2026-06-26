# Distilled Quran

A single-page interactive reader presenting scholarly summaries of all 114 souras of the Quran.

> **Note:** The Quran is eternally Arabic — this project works on an English translation. Summaries and TL;DRs are interpretations of the translated text, not the original Arabic.

**Live:** [raz123.github.io/quran-distill](https://raz123.github.io/quran-distill/)

## Features

- **114 souras** with scholarly summaries, one-line TL;DRs, and historical metadata
- **Chronological ordering** — view souras by revelation date (Meccan/Medinan)
- **Full-text search** across names and summaries
- **Responsive design** — works on mobile and desktop
- **Self-contained** — single `index.html`, no external dependencies

## Structure

```
index.html          # The entire app (HTML + CSS + JS + embedded data)
distilled_quran.md  # Full markdown companion document
```

## How it works

All data (114 soura summaries, metadata, TL;DRs) is embedded as JSON inside `index.html`. The app runs entirely client-side — no server required. Just open the file in a browser, or serve it with any static file server.

## Deployment

Hosted on GitHub Pages. Push to `main` and it auto-deploys.

```bash
python3 -m http.server 8080  # local dev
```

## Data sources

Summaries were generated from [risan/quran-json](https://github.com/risan/quran-json) and refined through multiple rounds of editorial and theological review.
