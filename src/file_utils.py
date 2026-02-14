"""File operations for puzzle tracking and output management."""
import json
import os
from pathlib import Path


def create_output_dir(output_path='output'):
    """Create output directory if it doesn't exist."""
    Path(output_path).mkdir(parents=True, exist_ok=True)


def load_used_puzzles(output_dir='output'):
    """Load the set of already-used puzzle IDs from tracking file."""
    tracking_file = os.path.join(output_dir, '.used_puzzles.json')
    if os.path.exists(tracking_file):
        try:
            with open(tracking_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_used_puzzles(used_puzzles, output_dir='output'):
    """Save the set of used puzzle IDs to tracking file."""
    tracking_file = os.path.join(output_dir, '.used_puzzles.json')
    with open(tracking_file, 'w', encoding='utf-8') as f:
        json.dump(used_puzzles, f, indent=2)
