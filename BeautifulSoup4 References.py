"""
BeautifulSoup4 Reference - bs4_reference.py
A full Python cheat sheet for parsing, navigating, and scraping HTML
"""

# -------------------------------
# 1. Setup
# -------------------------------
from bs4 import BeautifulSoup
import requests
import re

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")  # or "lxml"

# -------------------------------
# 2. Basic parsing
# -------------------------------
html_doc = "<html><body><p>Hello</p></body></html>"
soup2 = BeautifulSoup(html_doc, "html.parser")
print(soup2.prettify())  # Pretty print HTML

# -------------------------------
# 3. Searching the DOM
# -------------------------------
soup.find("title")          # First <title> tag
soup.find_all("p")          # All <p> tags
soup.find(id="main")        # Element with id="main"
soup.find_all(id="main")    
soup.find(class_="header")  
soup.find_all(class_="header")
soup.find("a", href="https://example.com")
soup.find_all("img", alt=True)

# -------------------------------
# 4. CSS selectors
# -------------------------------
soup.select("div.content")                # all divs with class "content"
soup.select("#main")                      # id selector
soup.select("div > p")                    # child selector
soup.select("ul li:nth-of-type(2)")      # nth child selector

# -------------------------------
# 5. Navigating the tree
# -------------------------------
tag = soup.find("div")
tag.text                                 # Get text
tag.get_text(strip=True)                 # Stripped text
tag.contents                             # Direct children list
list(tag.children)                        # Children generator to list
list(tag.descendants)                     # All nested tags
tag.parent
list(tag.parents)                         # All ancestor tags
tag.next_sibling
tag.previous_sibling
list(tag.next_siblings)
list(tag.previous_siblings)

# -------------------------------
# 6. Accessing attributes
# -------------------------------
a_tag = soup.find("a")
a_tag["href"]        # get attribute
a_tag.get("href")    # safer method
a_tag.attrs          # all attributes as dict

# -------------------------------
# 7. Searching with functions & regex
# -------------------------------
soup.find_all("a", href=re.compile("^https://"))  # regex on href

def has_data_id(tag):
    return tag.has_attr("data-id")
soup.find_all(has_data_id)

# -------------------------------
# 8. Traversing & filtering
# -------------------------------
soup.find_all("div", class_=lambda x: x and "product" in x)
soup.find_all("p", limit=5)  # Limit number of results

# -------------------------------
# 9. Extracting data safely
# -------------------------------
tag = soup.find("span", class_="price")
price = tag.text.strip() if tag else None

# -------------------------------
# 10. Handling dynamic sites (JS-rendered)
# -------------------------------
# BS4 cannot render JS. Use Selenium or Playwright for dynamic content.
# Example with Selenium:
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://example.com")
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# -------------------------------
# 11. Searching by text
# -------------------------------
soup.find_all(text="Buy now")            # exact match
soup.find_all(text=re.compile("Buy"))    # regex match

# -------------------------------
# 12. Modifying the DOM
# -------------------------------
tag = soup.find("p")
tag.string = "New text"
new_tag = soup.new_tag("span", **{"class": "highlight"})
new_tag.string = "Added span"
tag.append(new_tag)

# -------------------------------
# 13. Extracting lists of products
# -------------------------------
products = []
for div in soup.find_all("div", class_="product-card"):
    title = div.find("h2").text
    price = div.find("span", class_="price").text
    products.append({"title": title, "price": price})

# -------------------------------
# 14. Saving & loading HTML
# -------------------------------
# Save
with open("page.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Load
with open("page.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# -------------------------------
# 15. Debugging & testing
# -------------------------------
print(soup.prettify()[:500])   # Print first 500 chars
if soup.find("div", class_="price"):
    print("Found price")
