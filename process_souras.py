#!/usr/bin/env python3
"""Process Quran souras and generate summaries using AI."""

import json
from pathlib import Path
from typing import List, Dict

def load_quran() -> List[Dict]:
    """Load the Quran JSON data."""
    quran_path = Path(__file__).parent / "quran_en.json"
    with open(quran_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_soura_text(soura: Dict) -> str:
    """Extract all English text from a soura."""
    verses = []
    for verse in soura['verses']:
        verses.append(f"[{verse['id']}] {verse['translation']}")
    return "\n".join(verses)

def prepare_soura_batch(souras: List[Dict]) -> str:
    """Prepare a batch of souras for summarization."""
    batch_text = []
    for soura in souras:
        text = extract_soura_text(soura)
        batch_text.append(f"""
=== SOURA {soura['id']}: {soura['transliteration']} ({soura['translation']}) ===
Type: {soura['type']}
Total Verses: {soura['total_verses']}

{text}
""")
    return "\n".join(batch_text)

if __name__ == "__main__":
    quran = load_quran()
    print(f"Loaded {len(quran)} souras")
    
    # Example: process first 5 souras
    batch = prepare_soura_batch(quran[:5])
    print(batch[:2000])
