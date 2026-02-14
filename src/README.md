# Source Code Structure

This directory contains the modularized code for the Lichess Puzzles to PGN converter.

## Modules

### `file_utils.py`

File operations for puzzle tracking and output management.

**Functions:**

- `create_output_dir(output_path)` - Creates output directory if it doesn't exist
- `load_used_puzzles(output_dir)` - Loads previously used puzzle IDs from tracking file
- `save_used_puzzles(used_puzzles, output_dir)` - Saves used puzzle IDs to tracking file

### `pgn_utils.py`

PGN file creation utilities using python-chess library.

**Functions:**

- `create_pgn_from_puzzle(puzzle_data)` - Converts puzzle CSV data to PGN game format

### `puzzle_utils.py`

Puzzle filtering and utility functions.

**Functions:**

- `sanitize_filename(name)` - Sanitizes strings for safe use as filenames
- `puzzle_matches_keyword(puzzle_data, keyword)` - Checks if a puzzle matches the search keyword

### `parser.py`

Main CSV parsing and puzzle extraction logic.

**Functions:**

- `parse_csv_for_keyword(csv_file, keyword, output_dir)` - Parses CSV file and creates PGN output

## Usage

The modules are imported by the main `parse_puzzles.py` script in the project root.

```python
from src.parser import parse_csv_for_keyword
```

All modules use relative imports within the package for internal dependencies.
