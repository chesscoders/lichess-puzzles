"""Puzzle filtering and utility functions."""


def sanitize_filename(name):
    """Sanitize string to be used as filename."""
    # Replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name


def puzzle_matches_keyword(puzzle_data, keyword):
    """Check if puzzle matches the given keyword."""
    keyword_lower = keyword.lower()

    # Search in Themes
    themes = puzzle_data.get('Themes', '').lower()
    if keyword_lower in themes:
        return True

    # Search in OpeningTags
    opening_tags = puzzle_data.get('OpeningTags', '').lower()
    if keyword_lower in opening_tags:
        return True

    # Search in PuzzleId
    puzzle_id = puzzle_data.get('PuzzleId', '').lower()
    if keyword_lower in puzzle_id:
        return True

    return False
