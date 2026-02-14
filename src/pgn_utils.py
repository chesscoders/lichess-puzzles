"""PGN file creation utilities."""
import chess
import chess.pgn


def create_pgn_from_puzzle(puzzle_data):
    """Create a PGN game from puzzle data."""
    game = chess.pgn.Game()

    # Set up headers
    game.headers["Event"] = "Lichess Puzzle"
    game.headers["Site"] = puzzle_data.get('GameUrl', '')
    game.headers["Result"] = "*"
    game.headers["FEN"] = puzzle_data['FEN']
    game.headers["SetUp"] = "1"
    game.headers["PuzzleId"] = puzzle_data['PuzzleId']
    game.headers["Rating"] = puzzle_data.get('Rating', '')
    game.headers["Popularity"] = puzzle_data.get('Popularity', '')
    game.headers["NbPlays"] = puzzle_data.get('NbPlays', '')
    game.headers["Themes"] = puzzle_data.get('Themes', '')

    # Add opening tags if available
    if puzzle_data.get('OpeningTags', '').strip():
        game.headers["Opening"] = puzzle_data['OpeningTags']

    # Set up the board from FEN
    board = chess.Board(puzzle_data['FEN'])

    # Parse and add moves
    moves = puzzle_data['Moves'].strip().split()
    node = game

    for move_uci in moves:
        try:
            move = chess.Move.from_uci(move_uci)
            if move in board.legal_moves:
                node = node.add_variation(move)
                board.push(move)
            else:
                print(
                    f"Warning: Illegal move {move_uci} in puzzle {puzzle_data['PuzzleId']}")
                break
        except ValueError as e:
            print(
                f"Warning: Invalid move format {move_uci} in puzzle {puzzle_data['PuzzleId']}: {e}")
            break

    return game
