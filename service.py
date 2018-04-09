from model import *


def get_types():
    return Type.query.all()


def get_tables():
    return Book.query.all()


def drop_book(book_id):
    delbook = Book.query.filter(Book.id == book_id).first()
    dbs.delete(delbook)
    dbs.commit()


def save_book(id, title, author, published, pages, type_id):

    new_book = False
    if id is None:
        new_book = True
        book = Book()
    else:
        book = Book.query.filter(Book.id == id).first()
        if book is None:
            new_book = True

    book.title = title
    book.author = author
    book.date = published
    book.pages = pages
    book.type_id = int(type_id)

    if new_book:
        dbs.add(book)

    dbs.commit()


