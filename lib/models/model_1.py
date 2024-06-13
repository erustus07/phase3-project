from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Author(name='{self.name}')>"

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(title='{self.title}', author_id={self.author_id})>"

Author.books = relationship('Book', order_by=Book.id, back_populates='author')

class Checkout(Base):
    __tablename__ = 'checkouts'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    user_id = Column(Integer, primary_key=True)
    due_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Checkout(book_id={self.book_id}, user_id={self.user_id}, due_date={self.due_date})>"
