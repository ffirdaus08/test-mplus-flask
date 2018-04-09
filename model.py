from init import *


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date)
    pages = db.Column(db.Integer)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

    type = db.relationship('Type', foreign_keys=(type_id))

    def __iter__(self):
        yield 'id', self.id
        yield 'title', self.title
        yield 'author', self.author
        yield 'date', self.date
        yield 'pages', self.pages
        yield 'type_id', self.type_id


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)

    def __iter__(self):
        yield 'id', self.id
        yield 'title', self.title


auto_generate_tables = False

if auto_generate_tables:
    db.create_all()