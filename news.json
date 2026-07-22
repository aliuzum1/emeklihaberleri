import json
import urllib.request
import xml.etree.ElementTree as ET
import re

# SGK ve emekli haberleri kaynak adresi
rss_url = "https://news.google.com/rss/search?q=emekli+sgk+maas&hl=tr&gl=TR&ceid=TR:tr"

try:
    # Haberleri çek
    req = urllib.request.Request(
        rss_url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = urllib.request.urlopen(req)
    xml_data = response.read()

    # XML verisini işle
    root = ET.fromstring(xml_data)
    articles = []

    for item in root.findall('.//item'):
        title = item.find('title').text if item.find('title') is not None else ""
        link = item.find('link').text if item.find('link') is not None else ""
        description = item.find('description').text if item.find('description') is not None else ""
        pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ""
        
        # HTML etiketlerini temizle ve özeti kısalt
        clean_desc = re.sub('<[^<]+?>', '', description)
        if len(clean_desc) > 180:
            clean_desc = clean_desc[:180] + "..."

        articles.append({
            'title': title,
            'link': link,
            'description': clean_desc,
            'pubDate': pubDate
        })

    # news.json dosyasına kaydet
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
        
    print("Haberler başarıyla güncellendi.")

except Exception as e:
    print(f"Hata oluştu: {e}")
