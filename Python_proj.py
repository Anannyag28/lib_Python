import os

books = []

def load_books():
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            for line in file:
                title, author, genre = line.strip().split("|")
                books.append({"title": title, "author": author, "genre": genre})

def save_books():
    with open("books.txt", "w") as file:
        for book in books:
            file.write(f'{book["title"]}|{book["author"]}|{book["genre"]}\n')

def add_book():
    title = input("Enter book title: ").strip().title()
    author = input("Enter author name: ").strip().title()
    genre = input("Enter genre: ").strip().title()
    books.append({"title": title, "author": author, "genre": genre})
    print(f"'{title}' by {author} added.")

def view_books():
    if not books:
        print("No books in the shelf.")
        return
    print("\nBooks in the shelf:")
    for idx, book in enumerate(sorted(books, key=lambda x: x['title'])):
        print(f"{idx+1}. {book['title']} by {book['author']} [{book['genre']}]")

def search_book():
    query = input("Enter title to search: ").strip().lower()
    found = False
    for book in books:
        if query in book['title'].lower():
            print(f"Found: '{book['title']}' by {book['author']} [{book['genre']}]")
            found = True
    if not found:
        print("Book not found.")

def recommend_books():
    genre = input("Enter your favorite genre: ").strip().lower()
    recs = [book for book in books if genre in book['genre'].lower()]
    if recs:
        print(f"\nBooks in '{genre.title()}':")
        for book in recs:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("No recommendations found.")

def delete_book():
    title = input("Enter the title of the book to remove: ").strip().title()
    global books
    books = [book for book in books if book['title'] != title]
    print(f"'{title}' removed if it existed.")

def menu():
    load_books()
    while True:
        print("\nBOOKSHELF MENU")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Recommend by Genre")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            recommend_books()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            save_books()
            print("Shelf saved. Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
