from datetime import datetime
import json
from bs4 import BeautifulSoup
import requests


def fetch_sgk_news():
  url = "https://www.sgk.gov.tr/duyuru"
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      )
  }

  news_list = []
  try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")

      for item in soup.find_all("a", href=True):
        title = item.get_text(strip=True)
        link = item["href"]

        if title and len(title) > 15:
          if not link.startswith("http"):
            link = "https://www.sgk.gov.tr" + link

          keywords = ["emekli", "maaş", "sigorta", "prim", "tebliğ", "duyuru"]
          if any(kw in title.lower() for kw in keywords):
            if not any(n["title"] == title for n in news_list):
              news_list.append({
                  "title": title,
                  "link": link,
                  "date": datetime.now().strftime("%Y-%m-%d"),
              })
  except Exception as e:
    print(f"Hata: {e}")

  with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news_list[:15], f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
  fetch_sgk_news()
