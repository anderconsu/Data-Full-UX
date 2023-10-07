from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/all_books', methods=['GET'])
def all_books():
    return books

# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/v0/book_by_id', methods=['GET'])
def book_by_id():

    if "id" in request.args:
        
        result = []
        id = int(request.args['id'])
        for book in books:
            if book['id'] == id:
                result.append(book)
        
        if result == []:
            return "Id not found."
        
        else:
            return result
    
    else:
        return request.args


# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada utilzando al final del endpoint <string:title>
@app.route('/v0/book_by_id_str/<string:title>', methods=['GET'])
def book_by_id_str(title):

    results = [book for book in books if book['title'] == title]
    # results = []

    # for book in books:
    #     if book['title'] == title:
    #         results.append(book) 

    if results == []:
        return "Title not found."
    
    else:
        return results


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada

@app.route('/v0/book_by_title', methods=['GET'])
def book_by_title():

    if "title" in request.args:
        
        result = []
        title = request.args['title']
        for book in books:
            if book['title'] == title:
                result.append(book)
        
        if result == []:
            return "Title not found."
        
        else:
            return result
    
    else:
        return "You must provide a title parameter in the request."

# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/v0/add_book', methods=['POST'])
def add_book():

    new_book = request.get_json()
    books.append(new_book)

    return books

# 6.Ruta para añadir un libro mediante parámetros
@app.route('/v0/add_book_param', methods=['POST'])
def add_book_param():

    new_book = {}

    new_book['id'] = request.args.get('id')
    new_book['title'] = request.args.get('title')
    new_book['published'] = request.args.get('published')
    new_book['author'] = request.args.get('author')
    new_book['first_sentence'] = request.args.get('first_sentence')
    
    books.append(new_book)

    return books


# 7.Ruta para modificar un libro
@app.route('/v0/modify_book', methods=['PUT'])
def modify_book():

    id = int(request.args['id'])
    published = request.args['published']

    for book in books:
        if book['id'] == id:
            book['published'] = published
    
    return books

# 8.Ruta para eliminar un libro
@app.route('/v0/delete_book', methods=['DELETE'])
def delete_book():

    id = int(request.args['id'])

    for indx, book in enumerate(books):
        if book['id'] == id:
            books.remove(books[indx])
    
    return books

app.run()