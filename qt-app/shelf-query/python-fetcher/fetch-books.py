import requests
import csv
import random
import os
from datetime import datetime

# -----------------------------
# تنظیمات
# -----------------------------
QUERY = "programming"
MIN_YEAR = 2000
TOTAL_BOOKS = 50
MAX_PAGES = 25   # هرچی بیشتر → تنوع بیشتر

OUTPUT_FILE = "books.csv"


def fetch_books():
    """دریافت کتاب‌ها از OpenLibrary"""
    all_books = []
    seen = set()  # جلوگیری از تکراری‌ها

    for page in range(1, MAX_PAGES + 1):
        url = f"https://openlibrary.org/search.json?q={QUERY}&page={page}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request error on page {page}: {e}")
            continue

        data = response.json()
        docs = data.get("docs", [])

        if not docs:
            break

        for book in docs:
            year = book.get("first_publish_year")
            title = book.get("title")
            authors = ", ".join(book.get("author_name", []))

            if not title or not year:
                continue

            if year < MIN_YEAR:
                continue

            # جلوگیری از تکرار
            unique_key = (title, year)
            if unique_key in seen:
                continue

            seen.add(unique_key)

            all_books.append({
                "title": title.strip(),
                "author": authors.strip(),
                "year": year
            })

    return all_books


def save_to_csv(books):
    """ذخیره در فایل CSV"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, OUTPUT_FILE)

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(books)

    return file_path


def main():
    print("Fetching books...")
    books = fetch_books()

    if not books:
        print("No books found.")
        return

    # انتخاب تصادفی 50 کتاب
    selected = random.sample(books, min(TOTAL_BOOKS, len(books)))

    # مرتب‌سازی بر اساس سال
    selected.sort(key=lambda x: x["year"])

    # ذخیره
    file_path = save_to_csv(selected)

    print(f"Done. {len(selected)} books saved to:")
    print(file_path)


if __name__ == "__main__":
    main()
