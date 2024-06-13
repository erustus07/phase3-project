from lib.database import initialize_database, session
from lib.models.model_1 import Author, Book, Checkout
from lib.helpers import validate_date

def add_author(name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Author '{name}' added successfully.")

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
        print("2. Add Book")
        print("3. List Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Checkout Book")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            add_author(name)
        elif choice == '2':
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            add_book(title, author_id)
        elif choice == '3':
            list_books()
        elif choice == '4':
            book_id = input("Enter book ID to update: ")
            new_title = input("Enter new book title: ")
            update_book(book_id, new_title)
        elif choice == '5':
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        elif choice == '6':
            book_id = input("Enter book ID: ")
            user_id = input("Enter user ID: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            checkout_book(book_id, user_id, due_date)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


