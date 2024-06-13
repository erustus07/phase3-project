from lib.database import initialize_database, session
from lib.models.model_1 import Author, Book, Checkout

def print_all_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(author)

def print_all_books():
    books = session.query(Book).all()
    for book in books:
        print(book)

def print_all_checkouts():
    checkouts = session.query(Checkout).all()
    for checkout in checkouts:
        print(checkout)

if __name__ == "__main__":
    initialize_database()
    print("Authors:")
    print_all_authors()
    print("\nBooks:")
    print_all_books()
    print("\nCheckouts:")
    print_all_checkouts()
