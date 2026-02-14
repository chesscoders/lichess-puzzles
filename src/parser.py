"""CSV parsing and puzzle extraction logic."""
import csv
import os

from .file_utils import create_output_dir, load_used_puzzles, save_used_puzzles
from .pgn_utils import create_pgn_from_puzzle
from .puzzle_utils import sanitize_filename, puzzle_matches_keyword


def parse_csv_for_keyword(csv_file, keyword, output_dir='output'):
    """Parse CSV file and create a single PGN file with all puzzles matching the keyword."""
    create_output_dir(output_dir)

    # Load previously used puzzle IDs
    used_puzzles = load_used_puzzles(output_dir)
    keyword_used = set(used_puzzles.get(keyword, []))

    processed_count = 0
    skipped_count = 0
    output_count = 0
    total_matches = 0
    max_puzzles = 1000

    # Create temporary PGN file with all matching games
    temp_filename = sanitize_filename(f"{keyword}_puzzles_temp.pgn")
    temp_filepath = os.path.join(output_dir, temp_filename)

    output_puzzle_ids = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        # Skip empty lines at the beginning
        lines = (line for line in f if line.strip())
        reader = csv.DictReader(lines)

        with open(temp_filepath, 'w', encoding='utf-8') as pgn_file:
            for row in reader:
                processed_count += 1

                if puzzle_matches_keyword(row, keyword):
                    total_matches += 1
                    puzzle_id = row.get('PuzzleId', '')

                    # Skip if already used
                    if puzzle_id in keyword_used:
                        skipped_count += 1
                        continue

                    # Stop if we've reached the limit
                    if output_count >= max_puzzles:
                        continue

                    try:
                        game = create_pgn_from_puzzle(row)
                        print(game, file=pgn_file)

                        # Track this puzzle ID as used
                        output_puzzle_ids.append(puzzle_id)

                        # Add blank line between games (except after the last one)
                        if output_count < max_puzzles - 1:
                            print(file=pgn_file)

                        output_count += 1
                    except Exception as e:
                        print(
                            f"Error processing puzzle {puzzle_id}: {e}")

    if output_count == 0:
        print(f"\n✗ No new puzzles found matching keyword: '{keyword}'")
        print(
            f"Searched {processed_count} puzzles, skipped {skipped_count} already used")
        # Remove temporary file
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)
        return

    # Rename file to include last puzzle ID
    last_puzzle_id = output_puzzle_ids[-1] if output_puzzle_ids else 'unknown'
    final_filename = sanitize_filename(
        f"{keyword}_puzzles_{last_puzzle_id}.pgn")
    final_filepath = os.path.join(output_dir, final_filename)
    os.rename(temp_filepath, final_filepath)

    # Save the used puzzle IDs
    if keyword not in used_puzzles:
        used_puzzles[keyword] = []
    used_puzzles[keyword].extend(output_puzzle_ids)
    save_used_puzzles(used_puzzles, output_dir)

    print(f"\n✓ Output {output_count} puzzles to PGN file")
    new_matches = total_matches - skipped_count
    if new_matches > output_count:
        print(
            f"✓ Found {new_matches} new matches (limited output to {max_puzzles})")
    if skipped_count > 0:
        print(f"✓ Skipped {skipped_count} previously used puzzles")
    print(f"✓ Created single PGN file: {final_filepath}")
    print(f"Searched {processed_count} total puzzles")
