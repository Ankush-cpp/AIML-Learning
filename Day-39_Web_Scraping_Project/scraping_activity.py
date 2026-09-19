import requests
from bs4 import BeautifulSoup

# Scrape multiple pages and save HTML files

page_count = 1

while True:
    URL = f"https://quotes.toscrape.com/page/{page_count}/"

    res = requests.get(URL)

    soup = BeautifulSoup(res.text, "lxml")

    quotes = soup.select("div.quote")

    if not quotes:
        print("No valid pages anymore.")
        break

    with open(f"scraped_data/quotes{page_count}.html", "w", encoding="utf-8") as f:
        f.write(res.text)

    print(f"Downloaded data from page {page_count}")

    page_count += 1


# Read saved HTML file

with open("scraped_data/quotes1.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")


# Extract all quotes

all_quotes = soup.select("div.quote")

for quote in all_quotes:
    text = quote.select_one("span.text").get_text(strip=True)
    author = quote.select_one("small.author").get_text(strip=True)

    print("Quote:", text)
    print("Author:", author)
    print()


# Extract quotes having "life" tag

life_quotes = []

for quote in all_quotes:
    all_tags = []

    for tag in quote.select(".tags .tag"):
        all_tags.append(tag.get_text(strip=True))

    if "life" in all_tags:
        text = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)

        life_quotes.append([text, author])


print("Life Quotes:")

for quote in life_quotes:
    print("Quote:", quote[0])
    print("Author:", quote[1])
    print()