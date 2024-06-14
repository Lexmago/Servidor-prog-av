from flask_restful import Resource
# Este modulo irve para aceptar info de un usuario
from flask import request
#Importamos los metodos de nuestra API
from .methods import *

lista_objetos_almacen = [
{
    'id': 1,
    'nombre': 'Lapiz',
    'cantidad': 4
},
{
    'id': 2,
    'nombre': 'Goma',
    'cantidad': 3  
},
{
    'id': 3,
    'nombre': 'Tijeras',
    'cantidad': 6
}
]

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hola mundo desde la API', 'status': 200}
    
class Almacen(Resource):
    # Obtenemos la informacion del almacen
    def get(self):
        # Esta variable va a interceptar la información de nuestra Query
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')

        return buscar_elemento_id_nombre(lista_objetos_almacen, parametro_id, parametro_nombre)

    def post(self):
        # Se crea una nueva variable para guardar la información que posteó el usuario
        data = request.get_json()
        # Agregamos la información a la lista del almacén
        lista_objetos_almacen.append(data)

        return {'received': True, 'info': data, 'status': 200}
    
class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')