import requests
from bs4 import BeautifulSoup

def scrape_olx_books(subject_query, pages=1):
    results = []
    subject_query = subject_query.lower().strip().replace(" ", "-")

    for page in range(1, pages + 1):
        url = f"https://www.olx.uz/list/q-книга-{subject_query}/?page={page}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ошибка при подключении к OLX: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        ads = soup.find_all("a", href=True)
        found_ads = 0

        for ad in ads:
            href = ad['href']
            if "/d/obyavlenie/" in href and ad.text.strip():
                title = ad.text.strip()
                full_url = "https://www.olx.uz" + href if href.startswith("/") else href

               
                parent = ad.find_parent("div")
                price = "Цена не указана"
                if parent:
                    price_tag = parent.find("p")
                    if price_tag:
                        price = price_tag.get_text(strip=True)

                results.append({
                    "title": title,
                    "url": full_url,
                    "price": price
                })

                found_ads += 1
                if found_ads >= 10:
                    break

    return results

if __name__ == "__main__":
    subject = input("Введите предмет: ")
    ads = scrape_olx_books(subject, pages=1)

    if not ads:
        print("Ничего не найдено.")
    else:
        for ad in ads:
            print(f"{ad['title']} - {ad['price']}")
            print(f"Ссылка: {ad['url']}\n")

