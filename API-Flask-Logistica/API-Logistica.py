from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
import json
from datetime import datetime
from json import dumps
import pyodbc

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=serversqlferremas.database.windows.net;'
        'DATABASE=bdferremas;'
        'UID=adminFerremas;'
        'PWD=ContraseñaFerremas098'
    )
    return connection

class Logistica(Resource):
    def post(self):
        date = datetime.now()
        dt_str = date.strftime('%Y-%m-%d %H:%M:%S') 
        json_date = str(dt_str)
        data = request.get_json()
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_postPed ?, ?", ("Procesando compra", data['idBoleta']))
                connection.commit()
                return {'message': 'User created successfully'}, 201
        finally:
            connection.close()
    
    def get(self):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_getAllped")
                result = cursor.fetchall()
                users = [{'idPedido': row[0], 'nombreCli': row[1], 'estado': row[2], 'tipoEntrega': row[3], 'fechaBoleta': str(row[4])} for row in result]
                return users
        finally:
            connection.close()
    
class LogisticaById(Resource):
    def get(self, id):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_getPed ?", (id,))
                result = cursor.fetchone()
                if result:
                    return {'idPedido': result[0], 'nombreCli': result[1], 'estado': result[2], 'tipoEntrega': result[3], 'fechaBoleta': str(result[4])}
                return {'message': 'User not found'}, 404
        finally:
            connection.close()
    
    def put(self, id):
        data = request.get_json()
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_putPed ?, ?", (id, data['estado']))
                connection.commit()
                return {'message': 'User updated successfully'}
        finally:
            connection.close()
    

    def delete(self, id):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_deletePed ?", (id))
                connection.commit()
                return {'message': 'User deleted successfully'}
        finally:
            connection.close()



api.add_resource(Logistica, "/api/logistica/")
api.add_resource(LogisticaById, "/api/logistica/<int:id>")
app.run(debug=True, port=5003)
