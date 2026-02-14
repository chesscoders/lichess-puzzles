#!/usr/bin/env python3
"""
Parse Lichess puzzle CSV and generate a PGN file for puzzles matching a keyword.
"""
import argparse
import os

from src.parser import parse_csv_for_keyword


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search Lichess puzzle CSV by keyword and generate a PGN file.'
    )
    parser.add_argument(
        '--csv',
        required=True,
        help='Path to CSV file'
    )
    parser.add_argument(
        '--keyword',
        required=True,
        help='Search for puzzles matching this keyword and create a single PGN file'
    )

    args = parser.parse_args()

    if not os.path.exists(args.csv):
        print(f"Error: CSV file '{args.csv}' not found")
        exit(1)

    print(f"Parsing {args.csv}...")
    parse_csv_for_keyword(args.csv, args.keyword, 'output')
