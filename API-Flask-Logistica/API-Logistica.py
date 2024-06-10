from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
import json
from datetime import datetime
from json import dumps

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_boleta = "http://localhost:5002/api/boleta"

url_cliente = "http://localhost:14792/api/Cliente"

url_producto = "http://localhost:14792/api/Producto"

contador = -1

DatosLogistica = []

class Logistica(Resource):
    def post(self):
     
        global contador
        contador = contador + 1

        jsonn = request.get_json()

        cliente_response = requests.get(url_cliente+"/"+ str(jsonn["IdCli"]))
        producto_response = requests.get(url_producto+"/"+ str(jsonn["IdProd"]))
        print(cliente_response.status_code)
        if(cliente_response.status_code == 200 and producto_response.status_code == 200):
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()    
            date = datetime.now()
            dt_str = date.strftime('%Y-%m-%d %H:%M:%S') 
            json_date = json.dumps(dt_str)

            #id boleta, direccion, telefono, despacho a domicilio, fecha*, estado de envio

            txtEstado = "Procesando compra"

            lista = {
                "IdPedido": contador,
                "NombreCli": cliente_json["nombre"],
                "DireccionCli": cliente_json["direccion"],
                "NombreProd": producto_json["nombre"],
                "Cantidad": jsonn["Cantidad"],
                "TipodeEntrega": jsonn["DespachoDomicilio"],
                "Estado": txtEstado,
                "FechaPedido": json_date}


        else: 
            print("error")

        DatosLogistica.append(lista)
        return ""
    
    def get(self):
        return DatosLogistica
    
class LogisticaById(Resource):
    def get(self,id):
        return DatosLogistica[id]
    
    def put(self, id):
        jsonn = request.get_json()
        DatosLogistica[id]['Estado'] = jsonn['Estado']
        return DatosLogistica
    

    def delete(self, id):
        DatosLogistica.pop(id)
        return ""



api.add_resource(Logistica, "/api/logistica/")
api.add_resource(LogisticaById, "/api/logistica/<int:id>")
app.run(debug=True, port=5003)
