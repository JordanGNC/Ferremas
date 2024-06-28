from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
import json
from datetime import datetime
from json import dumps
import pyodbc

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

# Configura la conexión a la base de datos
def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=serversqlferremas.database.windows.net;'
        'DATABASE=bdferremas;'
        'UID=adminFerremas;'
        'PWD=ContraseñaFerremas098'
    )
    return connection

class Boleta(Resource):

    def post(self):
        query = "SELECT precio FROM producto WHERE idProducto = ?"
        date = datetime.now()
        dt_str = date.strftime('%Y-%m-%d %H:%M:%S') 
        json_date = str(dt_str)
        data = request.get_json()
        connection = get_db_connection()
        idProd = data['IdProd']
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, idProd)
                precio = cursor.fetchone()
                precio = str(precio).replace(',', '')
                precio = str(precio).replace(')', '')
                precio = str(precio).replace('(', '')
                precio = int(precio)
                total = data['Cantidad']*precio
                cursor.execute("EXEC p_postBol ?, ?, ?, ?, ?, ?", (data['Cantidad'], total , data['TipoEntrega'], json_date, data['IdCli'], idProd))
                connection.commit()
                return {'message': 'Boleta created successfully'}, 201
        finally:
            connection.close()
            
    
    def get(self):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_getAllBol")
                result = cursor.fetchall()
                users = [{'idBoleta': row[0], 'cantidad': row[1], 'total': row[2], 'tipoEntrega': row[3], 'fechaBoleta': str(row[4])} for row in result]
                return users
        finally:
            connection.close()

class BoletaById(Resource):
    def get(self, id):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_getBol ?", (id,))
                result = cursor.fetchone()
                if result:
                    return {'IdBoleta': result[0], 'Cantidad': result[1], 'Total': result[2], 'TipoEntrega': result[3], 'FechaBoleta': str(result[4])}
                return {'message': 'Boleta not found'}, 404
        finally:
            connection.close()
    
    def put(self, id):
        data = request.get_json()
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_putBol ?, ?, ?, ?", (id, data['Cantidad'], data['Cantidad'], data['TipoEntrega']))
                connection.commit()
                return {'message': 'Boleta updated successfully'}
        finally:
            connection.close()
    
    def delete(self, id):
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC p_deleteBol ?", (id))
                connection.commit()
                return {'message': 'Boleta deleted successfully'}
        finally:
            connection.close()
   
api.add_resource(Boleta, "/api/boleta/")
api.add_resource(BoletaById, "/api/boleta/<int:id>")

app.run(debug=True, port=5002)

        
