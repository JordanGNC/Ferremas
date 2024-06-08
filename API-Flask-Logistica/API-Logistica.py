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

contador = -1

DatosLogistica = []

class Logistica(Resource):
    def post(self):
     
        global contador
        contador = contador + 1

        jsonn = request.get_json()

        boleta_response = requests.get(url_boleta+"/"+ str(jsonn["IdBoleta"]))
        print(boleta_response.status_code)
        if(boleta_response.status_code == 200):
            boleta_json = boleta_response.json()

            #id boleta, direccion, telefono, despacho a domicilio, fecha*, estado de envio
            txtTipoEntrega = ""
            if boleta_json["DespachoDomicilio"] == True:
                txtTipoEntrega = "Despacho a domicilio"
            else: 
                txtTipoEntrega = "Retiro en tienda"

            txtEstado = ""
            if boleta_json["DespachoDomicilio"] == True:
                txtEstado = "En camino hacia su direccion: "+boleta_json["DireccionCli"]
            else:
                txtEstado = "Esperando el retiro en tienda de parte del cliente"

            lista = {
                "Idpedido": contador,
                "IdBoleta": boleta_json["IdBoleta"],
                "NombreCli": boleta_json["NombreCli"],
                "DireccionCli": boleta_json["DireccionCli"],
                "NombreProd": boleta_json["NombreProd"],
                "PrecioProd": boleta_json["PrecioProd"],
                "Cantidad": boleta_json["Cantidad"],
                "Total": boleta_json["Total"],
                "TipoDeEntrega": txtTipoEntrega,
                "Estado": txtEstado,
                "FechaBoleta": boleta_json["FechaBoleta"]}

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
        DatosLogistica.pop(id)

        jsonn = request.get_json()

        boleta_response = requests.get(url_boleta+"/"+ str(jsonn["IdBoleta"]))
        print(boleta_response.status_code)
        if(boleta_response.status_code == 200):
            boleta_json = boleta_response.json()

            #id boleta, direccion, telefono, despacho a domicilio, fecha*, estado de envio
            txtTipoEntrega = ""
            if boleta_json["DespachoDomicilio"] == True:
                txtTipoEntrega = "Despacho a domicilio"
            else: 
                txtTipoEntrega = "Retiro en tienda"

            txtEstado = ""
            if boleta_json["DespachoDomicilio"] == True:
                txtEstado = "En camino hacia su direccion: "+boleta_json["DireccionCli"]
            else:
                txtEstado = "Esperando el retiro en tienda de parte del cliente"

            lista = {
                "Idpedido": id,
                "IdBoleta": boleta_json["IdBoleta"],
                "NombreCli": boleta_json["NombreCli"],
                "DireccionCli": boleta_json["DireccionCli"],
                "NombreProd": boleta_json["NombreProd"],
                "PrecioProd": boleta_json["PrecioProd"],
                "Cantidad": boleta_json["Cantidad"],
                "Total": boleta_json["Total"],
                "TipoDeEntrega": txtTipoEntrega,
                "Estado": txtEstado,
                "FechaBoleta": boleta_json["FechaBoleta"]}

        else: 
            print("error")

        DatosLogistica.insert(id,lista)
        return ""
    

    def delete(self, id):
        DatosLogistica.pop(id)
        return ""



api.add_resource(Logistica, "/api/logistica/")
api.add_resource(LogisticaById, "/api/logistica/<int:id>")
app.run(debug=True, port=5003)
