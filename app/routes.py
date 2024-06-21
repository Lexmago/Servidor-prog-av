from flask_restful import Resource
# Este modulo irve para aceptar info de un usuario
from flask import request
#Importamos los metodos de nuestra API
from .methods import *


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hola mundo desde la API', 'status': 200}
    
class Almacen(Resource):
    # Obtenemos la informacion del almacen
    def get(self):
        # Esta variable va a interceptar la información de nuestra Query
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')

        return buscar_elemento_id_nombre(parametro_id, parametro_nombre)

    def post(self):
        # Se crea una nueva variable para guardar la información que posteó el usuario
        data = request.get_json()

        return crear_producto(data['nombre'], data['cantidad'])
    
    
class User_register(Resource):
    def post(self):
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        print(username, email, password)

        return 'Hola', 200

class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')
        api.add_resource(User_register, '/usuarios/registro')