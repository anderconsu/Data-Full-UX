import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = "SELECT * FROM books"
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return result

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/api/v1/resources/books_by_author/descend', methods=['GET'])
def books_count_descend():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = '''SELECT COUNT(title) AS Count, author
                        FROM books
                        GROUP BY author
                        ORDER BY Count DESC;'''
    result = cursor.execute(select_books).fetchall()
    connection.close()
    return result


# 2.Ruta para obtener los libros de un autor como argumento en la llamada
@app.route('/api/v1/resources/books/author_param', methods=['GET'])
def books_by_author_param():

    if "author" in request.args:

        author = "%" + request.args['author'] + "%"
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()

        select_books = '''SELECT title,author 
                            FROM books
                            WHERE ?;'''
        
        result = cursor.execute(select_books, ([author])).fetchall()
        connection.close()
        if result == []:
            return "Author not found"
        
        else:
            return result

    else:
        return "You must provide an 'author' parameter in your request."
    
# 3.Ruta para obtener los libros filtrados por título, publicación y autor
@app.route('/api/v1/resources/books/filter_books', methods=['GET'])
def filter_books():

    query = '''SELECT title, published, author
                        FROM books
                        WHERE '''
    filters = []
    if "author" in request.args:
        author = "%" + request.args.get('author') + "%"
        filters.append(author)
        query += "author LIKE ? AND "
    
    if "published" in request.args:
        published = "%" + request.args.get('published') + "%"
        filters.append(published)
        query += "published LIKE ? AND "

    
    if "title" in request.args:
        title = "%" + request.args.get('title') + "%"
        filters.append(title)
        query += "title LIKE ? AND "



    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    
        
    result = cursor.execute(query[:-4], (filters)).fetchall()
    connection.close()
    
    return result


app.run()