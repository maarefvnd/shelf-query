import requests
import csv

URL = "https://openlibrary.org/search.json?q=programming&limit=50"
OUTPUT_CSV = "books.csv"

def fetch_books(url):
    """کتاب‌ها رو از OpenLibrary می‌گیره و JSON برمی‌گردونه"""
    response = requests.get(url)
    response.raise_for_status()  # اگه خطایی بود ارور بده
    data = response.json()
    return data.get("docs", [])

def filter_books(books, min_year=2000):
    """کتاب‌هایی که بعد از min_year منتشر شدن رو نگه می‌داره"""
    filtered = []
    for book in books:
        year = book.get("first_publish_year")
        if year and year > min_year:
            filtered.append({
                "title": book.get("title"),
                "author": ", ".join(book.get("author_name", [])),
                "year": year
            })
    return filtered

def sort_by_year(book_list):
    """کتاب‌ها رو بر اساس سال انتشار صعودی مرتب می‌کنه"""
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]["year"] > book_list[j+1]["year"]:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]

def save_to_csv(book_list, filename):
    """لیست کتاب‌ها رو تو CSV ذخیره می‌کنه"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(book_list)

def main():
    books = fetch_books(URL)
    filtered_books = filter_books(books, min_year=2000)
    sort_by_year(filtered_books)
    save_to_csv(filtered_books, OUTPUT_CSV)
    print(f"Done. {len(filtered_books)} books saved to {OUTPUT_CSV}.")

if __name__ == "__main__":
    main()
