import psycopg2
from psycopg2 import Error
from flask import jsonify, Flask, make_response, request


class DBConnection:
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="97847335",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="Covid")
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print("Error while working with PostgreSQL", error)
            response = make_response(error)
            response.headers['Access-Control-Allow-Origin'] = '*'

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection closed")
