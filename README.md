# lib_Python
# Book Shelf Organizer

A basic command-line Python project to manage your personal book collection.

This project allows you to add, view, search, delete, and recommend books based on genre. It uses simple data structures like lists and dictionaries along with file handling to store book records.

## Features

- Add a book with title, author, and genre
- View all books (sorted by title)
- Search books by title (case-insensitive)
- Recommend books based on genre
- Delete a book by title
- Save and load book records using a text file

## Technologies Used

- Python 3
- No external libraries
- File handling with `.txt` files

## How It Works

1. The program loads saved book data from `books.txt` (if it exists).
2. Users interact through a menu in the terminal.
3. All book details are stored in a list of dictionaries.
4. On exit, the book list is saved to `books.txt` for future sessions.

## Sample Menu
BOOKSHELF MENU
1. Add Book
2. View All Books
3. Search Book
4. Recommend by Genre
5. Delete Book
6. Exit
Select an option (1-6): 



