<div align="center">

# 📖 Distilled Quran

**A scholarly summary of all 114 souras of the Quran**

[![Live Demo](https://img.shields.io/badge/Live-Distilled%20Quran-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://raz123.github.io/quran-distill/)

</div>

---

> **Note:** The Quran is eternally Arabic — this project works on an English translation. Summaries and TL;DRs are interpretations of the translated text, not the original Arabic.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📚 **114 Souras** | Scholarly summaries, one-line TL;DRs, and historical metadata |
| 📅 **Chronological Ordering** | View souras by revelation date (Meccan / Medinan) |
| 🔍 **Full-Text Search** | Search across soura names and summaries |
| 📱 **Responsive Design** | Works beautifully on mobile and desktop |
| 🚀 **Self-Contained** | Single `index.html` — no external dependencies |

## 🏗️ Structure

```
quran-distill/
├── index.html          # The entire app (HTML + CSS + JS + embedded data)
└── distilled_quran.md  # Full markdown companion document
```

## ⚙️ How It Works

All data — 114 soura summaries, metadata, and TL;DRs — is embedded as JSON inside `index.html`. The app runs entirely client-side with no server required. Just open the file in any modern browser.

## 🚢 Deployment

Hosted on **GitHub Pages**. Push to `main` and it auto-deploys.

```bash
# Local development
python3 -m http.server 8080
# → http://localhost:8080
```

## 📖 Data Sources

Summaries were generated from [risan/quran-json](https://github.com/risan/quran-json) and refined through multiple rounds of editorial and theological review.

---

<div align="center">

**Built with ❤️ for those who seek understanding**

</div>
