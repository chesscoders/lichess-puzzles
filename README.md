# Lichess Puzzles to PGN Converter

A Python script that parses Lichess puzzle CSV files and generates PGN files for puzzles matching a keyword.

## Features

- Converts Lichess puzzle CSV data into standard PGN format
- Search by keyword to create a single PGN file with multiple matching puzzles
- Tracks used puzzles - reruns with same keyword return fresh, unused puzzles
- Preserves puzzle metadata (rating, themes, game URL, opening tags)
- Validates moves using python-chess library

## Requirements

- Python 3.7+
- python-chess library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Search for puzzles by keyword and create a single PGN file:

```bash
python parse_puzzles.py --csv data/sample.csv --keyword endgame
```

This creates a single PGN file in the `output/` directory containing all puzzles that match the keyword. The filename includes the last PuzzleId to prevent overwrites (e.g., `endgame_puzzles_01Abc.pgn`). The keyword is searched in:

- Themes
- Opening tags
- Puzzle ID

### Command-line options

```bash
python parse_puzzles.py --csv CSV_FILE --keyword KEYWORD

Required:
  --csv PATH       Path to CSV file (required)
  --keyword TEXT   Search for puzzles matching this keyword (required)
```

## Examples

```bash
# Find all "mate" puzzles
python parse_puzzles.py --csv data/sample.csv --keyword mate

# Find all "endgame" puzzles
python parse_puzzles.py --csv data/sample.csv --keyword endgame

# Find all "fork" puzzles from custom CSV
python parse_puzzles.py --csv data/my_puzzles.csv --keyword fork
```

## Puzzle Tracking

The script tracks which puzzles have been outputted for each keyword in `output/.used_puzzles.json`. When you rerun the script with the same keyword:

- Previously used puzzles are automatically skipped
- Only new, unused puzzles matching the keyword are included
- Each keyword maintains its own list of used puzzles
- Each run creates a new file with the last PuzzleId in the filename (e.g., `mateIn2_puzzles_00Zo.pgn`, then `mateIn2_puzzles_01Ab.pgn`)

This ensures you get fresh datasets every time you run the script with the same keyword without overwriting previous files.

## CSV Format

The script expects a CSV file with the following columns:

- PuzzleId
- FEN
- Moves
- Rating
- RatingDeviation
- Popularity
- NbPlays
- Themes
- GameUrl
- OpeningTags

## Output

Each PGN file includes:

- Standard PGN headers (Event, Site, Result)
- Starting position (FEN)
- Puzzle metadata (ID, rating, themes)
- Solution moves in standard notation

## Project Structure

```txt
lichess-puzzles/
├── parse_puzzles.py      # Main entry point script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── data/                # CSV input files
├── output/              # Generated PGN files
└── src/                 # Source code modules
    ├── __init__.py
    ├── file_utils.py    # File operations & tracking
    ├── pgn_utils.py     # PGN creation logic
    ├── puzzle_utils.py  # Puzzle filtering utilities
    ├── parser.py        # Main parsing logic
    └── README.md        # Module documentation
```

The code is modularized for clarity and maintainability. See [src/README.md](src/README.md) for detailed module documentation.
