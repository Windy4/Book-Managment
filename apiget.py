import openai
import time
import requests

genres = ["science fiction", "fantasy", "mystery"]
all_books = []

# Function to query GPT for a genre
def get_books_by_genre(genre):
    url = f"https://openlibrary.org/subjects/{genre.lower().replace(' ', '_')}.json?limit=5"
    response = requests.get(url)
    data = response.json()

    books = []
    for book in data.get("works", []):
        title = book.get("title")
        author = book["authors"][0]["name"] if book.get("authors") else "Unknown"
        books.append((title, author))

    return books

# Parse GPT response
def parse_books(text):
    results = []
    lines = text.strip().split("\n")
    for line in lines:
        if " - " in line:
            title, author = line.split(" - ", 1)
            results.append({
                "title": title.strip(),
                "author": author.strip()
            })
    return results

# Main polling loop
for genre in genres:
    print(f"\nBooks for genre: {genre}")
    books = get_books_by_genre(genre)
    for title, author in books:
        print(f"{title} by {author}")
        all_books.append((title, author))

# Print results
print("\nCollected Book List:")
for b in books:
    print(f"{b[0]} by {b[1]}")
