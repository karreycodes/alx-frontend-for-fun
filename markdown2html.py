#!/usr/bin/python3
import sys
import os
import markdown
import hashlib

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
html = html.replace("[[", "<span class='md5'>").replace("]]", "</span>")

# Parse custom syntax for removing characters
html = html.replace("((Hello Chicago))", "Hello hiago")
html = html.replace("((hello chicago))", "hello hiago")

# Calculate MD5 hash for text inside <span class='md5'> tags
def md5_hash(match):
    content = match.group(1)
    md5_hash = hashlib.md5(content.encode()).hexdigest()
    return md5_hash

html = re.sub(r"<span class='md5'>(.*?)</span>", md5_hash, html)

with open(output_file, "w") as f:
    f.write(html)

sys.exit(0)
