import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/catalogue"


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser') if response.status_code == 200 else None


def get_book_details(book_url):
    soup = get_soup(book_url)
    if not soup:
        print("Error loading book details")
        return

    title = soup.find('h1').get_text(strip=True)
    price = soup.find('p', class_='price_color').get_text(
        strip=True).replace('Â', '').strip()
    description = soup.find('meta', {'name': 'description'})

    print(f"\nTitle: {title}\nPrice: {price}\nDescription: {
          description['content'].strip() if description else 'No description available'}")


def get_books_from_category(category_url):
    soup = get_soup(category_url)
    if not soup:
        print("Error loading category page")
        return

    books = soup.find_all('h3')
    book_links = [(book.find('a')['title'], f"{BASE_URL}{
                   book.find('a')['href'][8:]}") for book in books]

    print("\nBooks in this category:")
    for i, (title,_) in enumerate(book_links, 1):
        print(f"{i}. {title}")

    try:
        selected_book_url = book_links[int(
            input("\nEnter book number: ")) - 1][1]
        get_book_details(selected_book_url)
    except (IndexError, ValueError):
        print("Invalid selection")


def main():
    soup = get_soup("http://books.toscrape.com/")
    if not soup:
        print("Error loading page")
        return

    categories = soup.select('.side_categories a')[1:]
    category_links = [(cat.get_text(
        strip=True), f"http://books.toscrape.com/{cat['href']}") for cat in categories]

    for i, (name, _) in enumerate(category_links, 1):
        print(f"{i}. {name}")

    try:
        selected_category_url = category_links[int(
            input("\nEnter category number: ")) - 1][1]
        get_books_from_category(selected_category_url)
    except (IndexError, ValueError):
        print("Invalid selection")


if __name__ == "__main__":
    main()
