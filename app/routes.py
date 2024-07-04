from flask_restful import Resource
# Este modulo irve para aceptar info de un usuario
from flask import request
#Importamos los metodos de nuestra API
from .methods import *
from flask_jwt_extended import jwt_required, get_jwt_identity


class HelloWorld(Resource):
    #@jwt_required() # Decorador que protege la ruta raíz de mi aplicación
    def get(self):
        #identidad = get_jwt_identity()
        return {'message': f'Hola Bienvenido a la API!', 'status': 200}
    
class Almacen(Resource):
    # Obtenemos la informacion del almacen
    @jwt_required()
    def get(self):
        # Esta variable va a interceptar la información de nuestra Query
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')

        return buscar_elemento_id_nombre(parametro_id, parametro_nombre)

    @jwt_required()
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

        #print(username, email, password)
        respuesta, status = user_register(username, email, password)

        return respuesta, status
    
class User_login(Resource):
    def post(self):
        data = request.form
        email = data.get('email')
        password = data.get('password')

        respuesta, status = login(email, password)

        return respuesta, status


#Esta clase siempre debe ir al final de todo el codigo. Todo recurso despues de esta clase, ya no se ejecutará.
class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')
        api.add_resource(User_register, '/usuarios/registro')
        api.add_resource(User_login, '/usuarios/login')