# lib/cli.py

from lib.database import initialize_database, session
from lib.models.model_1 import Author, Book, Checkout
from lib.helpers import validate_date

def add_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Author '{name}' added successfully.")

def update_author(author_id, new_name):
    author = session.query(Author).filter(Author.id == author_id).first()
    if author:
        author.name = new_name
        session.commit()
        print(f"Author ID {author_id} updated successfully.")
    else:
        print(f"Author ID {author_id} not found.")

def delete_author(author_id):
    author = session.query(Author).filter(Author.id == author_id).first()
    if author:
        session.delete(author)
        session.commit()
        print(f"Author ID {author_id} deleted successfully.")
    else:
        print(f"Author ID {author_id} not found.")

def list_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(f"ID: {author.id}, Name: {author.name}")

def add_book(title, author_id):
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added successfully.")

def list_books():
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}")

def update_book(book_id, new_title):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = new_title
        session.commit()
        print(f"Book ID {book_id} updated successfully.")
    else:
        print(f"Book ID {book_id} not found.")

def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book ID {book_id} deleted successfully.")
    else:
        print(f"Book ID {book_id} not found.")

def checkout_book(book_id, user_id, due_date):
    validate_date(due_date)
    checkout = Checkout(book_id=book_id, user_id=user_id, due_date=due_date)
    session.add(checkout)
    session.commit()
    print(f"Book ID {book_id} checked out by User ID {user_id} until {due_date}.")

def main():
    initialize_database()
    while True:
        print("\nLibrary Management System")
        print("1. Add Author")
        print("2. Update Author")
        print("3. Delete Author")
        print("4. List Authors")
        print("5. Add Book")
        print("6. Update Book")
        print("7. Delete Book")
        print("8. List Books")
        print("9. Checkout Book")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            add_author(name)
        elif choice == '2':
            author_id = input("Enter author ID to update: ")
            new_name = input("Enter new author name: ")
            update_author(author_id, new_name)
        elif choice == '3':
            author_id = input("Enter author ID to delete: ")
            delete_author(author_id)
        elif choice == '4':
            list_authors()
        elif choice == '5':
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            add_book(title, author_id)
        elif choice == '6':
            book_id = input("Enter book ID to update: ")
            new_title = input("Enter new book title: ")
            update_book(book_id, new_title)
        elif choice == '7':
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        elif choice == '8':
            list_books()
        elif choice == '9':
            book_id = input("Enter book ID: ")
            user_id = input("Enter user ID: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            checkout_book(book_id, user_id, due_date)
        elif choice == '10':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
