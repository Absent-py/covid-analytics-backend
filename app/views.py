import psycopg2
from flask import jsonify, Flask, make_response, request
from flask_cors import CORS
from psycopg2 import Error

from app import app
from app.connection import DBConnection
from app.package import JPackage

CORS(app)


@app.route('/')
def index():
    return 'All is good'


@app.route('/execute', methods=['POST'])
def execute():
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


@app.route('/package/<table>')
def package(table):
    try:
        Connection = DBConnection()
        Connection.cursor.execute(f'SELECT Count(*) FROM "{table}"')
        response = Connection.cursor.fetchall()
        count = {'count': response[0][0]}
        Package = JPackage()
        headers = Package.setHeaders(count['count'])

        body = Package.setBody(table)
        obj = {
            'headers': headers,
            'body': body
        }
        return obj
    except (Exception, Error) as error:
        print(error)
    finally:
        del Connection
        del Package


@app.route('/death')
def death():
    try:
        Connection = DBConnection()
        response = Connection.getDeathInfo()
        percent = []
        count = 0
        death_c = 0
        alive_c = 0
        for item in response:
            death_c += item[1]
            alive_c += item[0]
            count += 1
            if (count % 29523) == 0:
                percent.append(death_c / (alive_c + 0.00000001) * 100)
                death_c = 0
                alive_c = 0
        return percent
    except (Exception, Error) as error:
        return error
    finally:
        if 'Connection' in locals():
            del Connection


@app.route('/death/diff')
def deathDiff():
    try:
        Connection = DBConnection()
        response = Connection.getDeathInfo()
        percent = []
        count = 0
        death_c = 0
        alive_c = 0
        for item in response:
            death_c += item[1]
            alive_c += item[0]
            count += 1
            if (count % 29523) == 0:
                percent.append(death_c / (alive_c + 0.00000001) * 100)
                death_c = 0
                alive_c = 0
        for i in range(99):
            percent[i] = percent[i + 1] - percent[i]
        percent[99] = 0
        print(percent)
        return percent
    except (Exception, Error) as error:
        return error
    finally:
        if 'Connection' in locals():
            del Connection
