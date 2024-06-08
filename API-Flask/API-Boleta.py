from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_cliente = "http://localhost:14792/api/Cliente"

url_producto = "http://localhost:14792/api/Producto"

contador = -1

DatosBoleta = []

class Boleta(Resource):
    
    def post(self):
     
        global contador
        contador = contador + 1

        json = request.get_json()

        cliente_response = requests.get(url_cliente+"/"+ str(json["IdCli"]))
        producto_response = requests.get(url_producto+"/"+ str(json["IdProd"]))
        print(cliente_response.status_code)
        if(cliente_response.status_code == 200 and producto_response.status_code == 200):
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()    

            lista = {
                "IdBoleta": contador,
                "IdCli": cliente_json["id"],
                "NombreCli": cliente_json["nombre"],
                "DireccionCli": cliente_json["direccion"],
                "IdProd": producto_json["id"],
                "NombreProd": producto_json["nombre"],
                "MarcaProd": producto_json["marca"],
                "TipoProd": producto_json["tipoProd"],
                "PrecioProd": producto_json["precio"],
                "Cantidad": json["Cantidad"],
                "Total": producto_json["precio"] * json["Cantidad"],
                "DespachoDomicilio": json["DespachoDomicilio"]}

            

        else: 
            print("error")

        DatosBoleta.append(lista)

        return ""
    
    def get(self):
        return DatosBoleta

class BoletaById(Resource):
    def get(self,id):
        return DatosBoleta[id]
    
    def put(self,id):
        DatosBoleta.pop(id)

        #Definir datos de la boleta

        json = request.get_json()

        cliente_response = requests.get(url_cliente+"/"+ str(json["IdCli"]))
        producto_response = requests.get(url_producto+"/"+ str(json["IdProd"]))
        print(cliente_response.status_code)
        if(cliente_response.status_code == 200 and producto_response.status_code == 200):
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()    

            lista = {
                "IdBoleta": id,
                "IdCli": cliente_json["id"],
                "NombreCli": cliente_json["nombre"],
                "DireccionCli": cliente_json["direccion"],
                "IdProd": producto_json["id"],
                "NombreProd": producto_json["nombre"],
                "MarcaProd": producto_json["marca"],
                "TipoProd": producto_json["tipoProd"],
                "PrecioProd": producto_json["precio"],
                "Cantidad": json["Cantidad"],
                "Total": producto_json["precio"] * json["Cantidad"],
                "DespachoDomicilio": json["DespachoDomicilio"]}

        else: 
            print("error")

        DatosBoleta.insert(id,lista)
        return ""
    
    def delete(self, id):
        DatosBoleta.pop(id)
        return ""
   
api.add_resource(Boleta, "/api/boleta/")
api.add_resource(BoletaById, "/api/boleta/<int:id>")

app.run(debug=True, port=5002)

        
