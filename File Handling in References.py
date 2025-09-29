"""
Python File Handling Reference - file_handling_reference.py
Covers:
- File reading/writing
- JSON handling
- Binary files
- Directories
- Temp files
- Regex (re)
"""

# -------------------------------
# 1. Imports
# -------------------------------
import os
import json
import re
import tempfile
import shutil
from pathlib import Path

# -------------------------------
# 2. File Reading
# -------------------------------
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()            # read entire file

with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()         # read all lines as list

for line in lines:
    print(line.strip())

# Read large files in chunks
with open("bigfile.txt", "r") as f:
    while chunk := f.read(1024):  # 1024 bytes at a time
        pass  # process(chunk)

# -------------------------------
# 3. File Writing
# -------------------------------
# Overwrite
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello world\nSecond line")

# Append
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# -------------------------------
# 4. JSON Handling
# -------------------------------
data = {"name": "Alice", "age": 25, "products": ["book", "pen"]}

# Write JSON to file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Read JSON from file
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

# JSON string conversions
json_str = json.dumps(data)
dict_data = json.loads(json_str)

# -------------------------------
# 5. Binary Files
# -------------------------------
with open("file.bin", "wb") as f:
    f.write(b"binary data")

with open("file.bin", "rb") as f:
    binary_data = f.read()

# -------------------------------
# 6. Creating and Deleting Files
# -------------------------------
# Create empty files
with open("newfile.txt", "w") as f: pass
Path("anotherfile.txt").touch()

# Delete files
os.remove("newfile.txt")
Path("anotherfile.txt").unlink()

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")
if Path("file.txt").exists():
    print("Exists")

# -------------------------------
# 7. Directories
# -------------------------------
# Create directories
os.mkdir("mydir")
os.makedirs("parent/child", exist_ok=True)

# List files
files = os.listdir("mydir")
print(files)

# Delete directories
os.rmdir("mydir")                 # only empty dir
shutil.rmtree("parent")           # recursively delete

# -------------------------------
# 8. Temporary Files
# -------------------------------
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"Temporary data")
    print(tmp.name)

# -------------------------------
# 9. Regex (re)
# -------------------------------
text = "Price: ₹1299"

# Search pattern
match = re.search(r"\d+", text)
if match:
    print(match.group())  # 1299

# Find all matches
numbers = re.findall(r"\d+", "123 apples, 45 oranges")
print(numbers)  # ['123', '45']

# Replace text
text2 = re.sub(r"\d+", "XXX", "Price: 1299")
print(text2)  # "Price: XXX"

# Match beginning
if re.match(r"^Buy", "Buy now"):
    print("Starts with Buy")

# Custom function example
def has_digits(s):
    return bool(re.search(r"\d+", s))
print(has_digits("abc123"))  # True
