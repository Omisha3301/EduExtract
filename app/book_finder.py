import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def find_books_on_amazon(book_titles):
    base_url = "https://www.amazon.in/s?k="
    results = []

    for title in book_titles:
        query = urllib.parse.quote_plus(title)
        search_url = base_url + query

        try:
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the first book result container
            first_result = soup.find('div', {'data-component-type': 's-search-result'})

            if not first_result:
                results.append({
                    "title": title,
                    "url": search_url,
                    "price": "Not Found",
                    "author": "Not Found",
                    "image": None
                })
                continue

            # Extract details
            link_tag = first_result.find('a', class_='a-link-normal', href=True)
            full_link = "https://www.amazon.in" + link_tag['href'] if link_tag else search_url

            title_tag = first_result.find('span', class_='a-size-medium')
            author_tag = first_result.find('div', class_='a-row a-size-base a-color-secondary')
            price_tag = first_result.find('span', class_='a-price-whole')
            image_tag = first_result.find('img', class_='s-image')

            results.append({
                "title": title_tag.text.strip() if title_tag else title,
                "url": full_link,
                "price": price_tag.text.strip() + " ₹" if price_tag else "Price not listed",
                "author": author_tag.text.strip() if author_tag else "Unknown",
                "image": image_tag['src'] if image_tag else None
            })

            time.sleep(1.5)  # Be nice to Amazon: avoid rate-limiting

        except Exception as e:
            print(f"Error fetching book '{title}': {e}")
            results.append({
                "title": title,
                "url": search_url,
                "price": "Error",
                "author": "Error",
                "image": None
            })

    return results
