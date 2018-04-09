from flask import Flask , Response, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import json

# KONEKSI KE SQLACHEMY


def _get_app():
    db_name = 'books'    # database name
    db_uri = 'mysql+pymysql://root:root@localhost:3306/' + db_name

    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_POOL_SIZE'] = 10
    flask_app.config['SQLALCHEMY_ECHO'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_db = SQLAlchemy(flask_app)

    return flask_app, flask_db


(app, db) = _get_app()
dbs = db.session


class JsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')

        return json.JSONEncoder.default(self, obj)


class EasyResponse:

    CODE_ERROR = -1
    CODE_SUCCESS = 0
    CODE_UNAUTHORIZED = 1

    def __init__(self, data=None):
        self.data = data
        self.code = self.CODE_SUCCESS
        self.message = 'success'
        self.status = {}

    def __iter__(self):
        self.status = {'code': self.code, 'message': self.message}
        yield 'data', self.data
        yield 'status', self.status

    def get_json_response(self):
        return Response(json.dumps(dict(self), cls=JsonEncoder), mimetype='application/json')


def objects_to_dict(_list):
    i = 0
    for obj in _list:
        _list[i] = dict(obj)
        i += 1

    return _list


def get_param(key):
    if key is None:
        return None

    return request.get_json().get(key)
