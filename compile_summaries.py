#!/usr/bin/env python3
"""Compile all batch summaries into a single document."""

import json
from pathlib import Path
from typing import List, Dict

def load_all_summaries() -> List[Dict]:
    """Load all batch summary files and compile them."""
    summaries_dir = Path(__file__).parent / "summaries"
    all_summaries = []

    for batch_num in range(1, 13):
        batch_file = summaries_dir / f"batch_{batch_num:02d}_summaries.json"
        if batch_file.exists():
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                # Handle different JSON structures
                if isinstance(batch_data, list):
                    all_summaries.extend(batch_data)
                elif isinstance(batch_data, dict):
                    # Try various keys that might contain the summaries
                    for key in ['summaries', 'souras', 'batch_info']:
                        if key in batch_data:
                            items = batch_data[key]
                            if isinstance(items, list):
                                all_summaries.extend(items)
                                break
                    else:
                        # If no known key, try to extract individual souras
                        for key, value in batch_data.items():
                            if isinstance(value, dict) and 'id' in value:
                                all_summaries.append(value)

    # Sort by soura ID
    all_summaries.sort(key=lambda x: x.get('id', 0))
    return all_summaries

def create_markdown(summaries: List[Dict]) -> str:
    """Create a markdown document from summaries."""
    lines = []
    lines.append("# The Distilled Quran")
    lines.append("")
    lines.append("## Chapter-by-Chapter Summary")
    lines.append("")
    lines.append("This document provides scholarly summaries for each of the 114 souras (chapters) of the Quran, using the Sahih International English translation as the reference text.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for summary in summaries:
        soura_id = summary.get('id', 'Unknown')
        name = summary.get('name', summary.get('transliteration', 'Unknown'))
        translation = summary.get('translation', summary.get('translation', ''))
        soura_type = summary.get('type', 'Unknown')
        total_verses = summary.get('total_verses', summary.get('verses', 'Unknown'))

        lines.append(f"## Soura {soura_id}: {name}")
        if translation and translation != name:
            lines.append(f"**English Name:** {translation}")
        lines.append(f"**Type:** {soura_type.capitalize()}")
        lines.append(f"**Total Verses:** {total_verses}")
        lines.append("")

        # Get the summary text
        summary_text = summary.get('summary', summary.get('text', ''))
        if summary_text:
            lines.append(summary_text)
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)

def main():
    print("Loading all batch summaries...")
    summaries = load_all_summaries()
    print(f"Loaded {len(summaries)} soura summaries")

    # Save compiled JSON
    compiled_json_path = Path(__file__).parent / "compiled_summaries.json"
    with open(compiled_json_path, 'w', encoding='utf-8') as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)
    print(f"Saved compiled JSON to {compiled_json_path}")

    # Create markdown
    markdown = create_markdown(summaries)
    markdown_path = Path(__file__).parent / "distilled_quran.md"
    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Saved markdown to {markdown_path}")

    # Print stats
    print(f"\nStatistics:")
    print(f"  Total souras: {len(summaries)}")
    print(f"  Markdown size: {len(markdown)} characters")
    print(f"  JSON size: {compiled_json_path.stat().st_size} bytes")

if __name__ == "__main__":
    main()
