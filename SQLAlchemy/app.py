from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Book

app = Flask(__name__)
engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/books')
def showBooks():
    books = session.query(Book).all()
    return render_template("books.html", books=books)


@app.route('/books/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newBook = Book(title=request.form['name'], author=request.form['author'], genre = request.form['genre'])
        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template('newBook.html')


@app.route('/books/edit/<book_id>', methods=['GET', 'POST'])
def editBook(book_id):
    bookToEdite = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editBook.title = request.form['name']
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html', book=bookToEdite)

@app.route('/books/delete/<book_id>', methods=['GET', 'POST'])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(bookToDelete)
        session.commit()
        return redirect(url_for('showBooks', book_id=book_id))
    else:
        return render_template('deleteBook.html', book=bookToDelete)


if __name__ == '__main__':
    app.debug = False
    app.run()