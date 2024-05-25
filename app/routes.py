from flask_restful import Resource

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
        return {'Objetos': lista_objetos_almacen, 'status': 200}
    # Ponemos un nuevo objeto en el almacen
    def post(self):
        return {'received': True, 'status': 200}
    
class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
        api.add_resource(Almacen, '/objetos_almacen')