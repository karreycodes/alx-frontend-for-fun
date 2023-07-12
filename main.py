#!/usr/bin/python3

import subprocess
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        subprocess.check_call(["python", "markdown2html.py", input_file, output_file])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
