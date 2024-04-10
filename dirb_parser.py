#!/usr/bin/env python3

import sys

def extract_useful_lines(output):
    useful_lines = []
    lines = output.split('\n')
    for line in lines:
        if line.startswith("----") or line.startswith("==>") or "CODE:200" in line:
            if useful_lines and not useful_lines[-1].startswith(("----", "==>", "CODE:200")):
                useful_lines.append("")  # Insert a blank line before the important lines
            useful_lines.append(line)
    return useful_lines

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dirb_parser.py <dirb_output_file>")
        sys.exit(1)
    
    # Read the DIRB output file
    dirb_output_file = sys.argv[1]
    with open(dirb_output_file, 'r') as f:
        dirb_output = f.read()

    useful_lines = extract_useful_lines(dirb_output)
    for line in useful_lines:
        print(line)
