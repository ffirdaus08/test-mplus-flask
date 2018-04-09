from service import *


@app.route('/',  methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/get-types',  methods=['POST'])
def api_get_types():
    types = get_types()
    types = objects_to_dict(types)

    res = EasyResponse(types)

    return res.get_json_response()


@app.route('/api/get-books',  methods=['POST'])
def api_get_table():
    tables = get_tables()
    tables = objects_to_dict(tables)

    res = EasyResponse(tables)

    return res.get_json_response()


@app.route('/api/book/save', methods=['POST'])
def api_saves():

    book_id = get_param('id')
    title = get_param('title')
    author = get_param('author')
    published = get_param('date')
    pages = get_param('pages')
    type_id = get_param('type_id')

    save_book(book_id, title, author, published, pages, type_id)

    return EasyResponse().get_json_response()


@app.route('/api/book/drop', methods=['POST'])
def api_drop_book():
    book_id = get_param('id')
    drop_book(book_id)

    return EasyResponse().get_json_response()
