# scraper.py
import requests
from bs4 import BeautifulSoup

def get_quotes():
    url = 'https://quotes.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    for quote in soup.find_all('span', class_='text'):
        quotes.append(quote.text)

    return quotes

if __name__ == '__main__':
    quotes = get_quotes()
    for i, quote in enumerate(quotes, start=1):
        print(f'{i}. {quote}')