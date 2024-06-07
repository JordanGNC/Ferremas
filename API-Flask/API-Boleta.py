from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url_cliente = "http://localhost:14792/api/Cliente"

url_producto = "http://localhost:14792/api/Producto"

class Boleta(Resource):
    def post(self):

        #Definir datos de la boleta
        DatosBoleta = {
            "IdCli": 0,
            "NombreCli": "",
            "DireccionCli": "",
            "IdProd": 0,
            "NombreProd": "",
            "MarcaProd": "",
            "TipoProd": "",
            "PrecioProd": 0,
            "Cantidad": 0,
            "Total": 0
        }

        json = request.get_json()

        cliente_response = requests.get(url_cliente+"/"+ str(json["IdCli"]))
        producto_response = requests.get(url_producto+"/"+ str(json["IdProd"]))
        print(cliente_response.status_code)
        if(cliente_response.status_code == 200 and producto_response.status_code == 200):
            cliente_json = cliente_response.json()
            producto_json = producto_response.json()

            DatosBoleta["IdCli"] = cliente_json["id"]
            DatosBoleta["NombreCli"] = cliente_json["nombre"]
            DatosBoleta["DireccionCli"] = cliente_json["direccion"]
            DatosBoleta["IdProd"] = producto_json["id"]
            DatosBoleta["NombreProd"] = producto_json["nombre"]
            DatosBoleta["MarcaProd"] = producto_json["marca"]
            DatosBoleta["TipoProd"] = producto_json["tipoProd"]
            DatosBoleta["PrecioProd"] = producto_json["precio"]
            DatosBoleta["Cantidad"] = json["Cantidad"]
            DatosBoleta["Total"] = producto_json["precio"] * json["Cantidad"]

        else: 
            print("error")

        return DatosBoleta
    
    
api.add_resource(Boleta, "/api/boleta")

app.run(debug=True, port=5001)

        
