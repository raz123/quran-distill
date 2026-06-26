#!/usr/bin/env python3
"""Generate summaries for all 114 Quran souras."""

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

def create_batch_file(souras: List[Dict], batch_num: int) -> str:
    """Create a batch file for processing."""
    batch_content = []
    for soura in souras:
        text = extract_soura_text(soura)
        batch_content.append(f"""
=== SOURA {soura['id']}: {soura['transliteration']} ({soura['translation']}) ===
Type: {soura['type']}
Total Verses: {soura['total_verses']}

{text}
""")
    return "\n".join(batch_content)

def main():
    quran = load_quran()
    print(f"Loaded {len(quran)} souras")

    # Split into batches of 10
    batch_size = 10
    batches = []
    for i in range(0, len(quran), batch_size):
        batch = quran[i:i+batch_size]
        batches.append(batch)

    print(f"Created {len(batches)} batches")

    # Create batch files
    output_dir = Path(__file__).parent / "batches"
    output_dir.mkdir(exist_ok=True)

    for i, batch in enumerate(batches):
        batch_file = output_dir / f"batch_{i+1:02d}.txt"
        batch_content = create_batch_file(batch, i+1)
        with open(batch_file, 'w', encoding='utf-8') as f:
            f.write(batch_content)
        print(f"Created {batch_file.name} with {len(batch)} souras")

    # Create manifest
    manifest = {
        "total_souras": len(quran),
        "batch_size": batch_size,
        "num_batches": len(batches),
        "batches": [
            {
                "batch_num": i+1,
                "soura_range": f"{batch[0]['id']}-{batch[-1]['id']}",
                "soura_names": [s['transliteration'] for s in batch]
            }
            for i, batch in enumerate(batches)
        ]
    }

    manifest_path = output_dir / "manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(f"Created manifest at {manifest_path}")

if __name__ == "__main__":
    main()
