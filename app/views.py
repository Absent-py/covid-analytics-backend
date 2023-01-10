import psycopg2
from flask import jsonify, Flask, make_response, request
from flask_cors import CORS
from psycopg2 import Error

from app import app
from app.connection import DBConnection

CORS(app)


@app.route('/')
def index():
    return 'All is good'


@app.route('/execute', methods=['POST'])
def execute():
    print('lol')
    try:
        query = request.json['query']
        print(query)
        if query != '':
            Connection = DBConnection()
            Connection.cursor.execute(query)
            data = {'data': Connection.cursor.fetchall()}
            json_data = jsonify(data=data['data'])
            response = make_response(json_data)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
        else:
            return 'None'
    except (Exception, Error) as error:
        print("Execute error", error)
        response = make_response(error)
        response.headers['Access-Control-Allow-Origin'] = '*'
    finally:
        if 'Connection' in locals():
            del Connection


@app.route('/package')
def package():
    print('package')
    try:
        Connection = DBConnection()
        Connection.cursor.execute('SELECT Count(*) FROM "Resist"')
        response = Connection.cursor.fetchall()
        print(response)
        return response
    except (Exception, Error) as error:
        print(error)
    finally:
        del Connection
