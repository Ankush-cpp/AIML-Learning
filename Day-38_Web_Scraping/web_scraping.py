import requests
from bs4 import BeautifulSoup
import time

url = "https://example.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()

    print("Status Code:", response.status_code)

    html = response.text

    with open("scraped_data/data.html", "w", encoding="utf-8") as file:
        file.write(html)

    soup = BeautifulSoup(html, "html.parser")

    print("Title:", soup.title.text)

    print("\nHeadings:")
    for heading in soup.find_all(["h1", "h2", "h3"]):
        print(heading.get_text(strip=True))

    print("\nLinks:")
    for link in soup.find_all("a"):
        print(link.get_text(strip=True), link.get("href"))

    time.sleep(1)

except requests.exceptions.RequestException as e:
    print("Error:", e)
    