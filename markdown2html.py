#!/usr/bin/python3
import sys
import os
import markdown
import hashlib
import re

def parse_md5(match):
    content = match.group(1)
    md5_hash = hashlib.md5(content.encode()).hexdigest()
    return md5_hash

def parse_removal(match):
    content = match.group(1)
    modified_content = re.sub(r'[cC]', '', content)
    return modified_content

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, "r") as f:
    markdown_text = f.read()

html = markdown.markdown(
    markdown_text,
    extensions=["markdown.extensions.extra", "markdown.extensions.nl2br"]
)

# Parse custom syntax for MD5 conversion
html = re.sub(r"\[\[(.*?)\]\]", parse_md5, html)

# Parse custom syntax for removing characters
html = re.sub(r"\(\((.*?)\)\)", parse_removal, html, flags=re.IGNORECASE)

with open(output_file, "w") as f:
    f.write(html)

sys.exit(0)
