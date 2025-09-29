"""
Python Reference - python_reference.py
All-in-one cheat sheet for:
- File handling
- JSON handling
- BeautifulSoup (BS4) parsing
- Regex usage (re)
- Basic web scraping
"""

# -------------------------------
# 1. Imports
# -------------------------------
import os
import json
import re
import requests
from bs4 import BeautifulSoup

# -------------------------------
# 2. File Handling
# -------------------------------

# Reading files
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())

# Writing files
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello world\nSecond line")
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\nAppended line")

# JSON handling
data = {"name": "Alice", "age": 25, "products": ["book", "pen"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
json_str = json.dumps(data)
dict_data = json.loads(json_str)

# Binary files
with open("file.bin", "wb") as f:
    f.write(b"binary data")
with open("file.bin", "rb") as f:
    data_bin = f.read()

# Create/Delete files
with open("newfile.txt", "w") as f: pass
from pathlib import Path
Path("anotherfile.txt").touch()
os.remove("newfile.txt")
Path("anotherfile.txt").unlink()

# Check file existence
if os.path.exists("file.txt"):
    print("File exists")
if Path("file.txt").exists():
    print("Exists")

# Directories
os.mkdir("mydir")
os.makedirs("parent/child", exist_ok=True)
files = os.listdir("mydir")
os.rmdir("mydir")
import shutil
shutil.rmtree("parent")

# Temporary files
import tempfile
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tmp.write(b"Temporary data")
    print(tmp.name)

# Large files read
with open("bigfile.txt", "r") as f:
    while chunk := f.read(1024):
        pass  # process(chunk)

# -------------------------------
# 3. Regex (re)
# -------------------------------
text = "Price: ₹1299"
match = re.search(r"\d+", text)
if match:
    print(match.group())
numbers = re.findall(r"\d+", "123 apples, 45 oranges")
text2 = re.sub(r"\d+", "XXX", "Price: 1299")
if re.match(r"^Buy", "Buy now"):
    print("Starts with Buy")

# -------------------------------
# 4. BeautifulSoup4 (BS4)
# -------------------------------
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")  # or "lxml"

# Parsing
html_doc = "<html><body><p>Hello</p></body></html>"
soup2 = BeautifulSoup(html_doc, "html.parser")
print(soup2.prettify())

# Searching
soup.find("title")
soup.find_all("p")
soup.find(id="main")
soup.find_all(class_="header")
soup.find("a", href="https://example.com")

# CSS selectors
soup.select("div.content")
soup.select("#main")
soup.select("div > p")
soup.select("ul li:nth-of-type(2)")

# Navigating
tag = soup.find("div")
tag.text
tag.get_text(strip=True)
tag.contents
list(tag.children)
list(tag.descendants)
tag.parent
list(tag.parents)
tag.next_sibling
tag.previous_sibling
list(tag.next_siblings)
list(tag.previous_siblings)

# Attributes
a_tag = soup.find("a")
a_tag["href"]
a_tag.get("href")
a_tag.attrs

# Regex & functions in find_all
soup.find_all("a", href=re.compile("^https://"))
def has_data_id(tag): return tag.has_attr("data-id")
soup.find_all(has_data_id)

# Traversing & filtering
soup.find_all("div", class_=lambda x: x and "product" in x)
soup.find_all("p", limit=5)

# Safe extraction
tag = soup.find("span", class_="price")
price = tag.text.strip() if tag else None

# Searching by text
soup.find_all(text="Buy now")
soup.find_all(text=re.compile("Buy"))

# Modifying DOM
tag = soup.find("p")
tag.string = "New text"
new_tag = soup.new_tag("span", **{"class": "highlight"})
new_tag.string = "Added span"
tag.append(new_tag)

# Extracting multiple products
products = []
for div in soup.find_all("div", class_="product-card"):
    title = div.find("h2").text
    price = div.find("span", class_="price").text
    products.append({"title": title, "price": price})

# Saving & loading HTML
with open("page.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
with open("page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Debugging
print(soup.prettify()[:500])
if soup.find("div", class_="price"):
    print("Found price")

# -------------------------------
# 5. Notes for dynamic JS content
# -------------------------------
# Use Selenium or Playwright to render JS before passing to BeautifulSoup:
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://example.com")
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
