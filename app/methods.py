from app.extensions import db
from .models.producto import Producto

def buscar_elemento_id_nombre(parametro_id, parametro_nombre):
    if parametro_id != None:

        producto_obtenido = Producto.query.get_or_404(parametro_id)

        json_retornado = {
            'ID': producto_obtenido.id,
            'Nombre': producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }
    
        return json_retornado
    
    elif parametro_nombre != None:
        producto_obtenido = Producto.query.filter_by(nombre=parametro_nombre).first_or_404()

        json_retornado = {
            'ID': producto_obtenido.id,
            'Nombre': producto_obtenido.nombre,
            'Cantidad': producto_obtenido.cantidad
        }

        return json_retornado
    
    else:
        return {'Error': 'No pusiste ninguna Query'}, 500 # 500 de internal server error
    
def crear_producto(nombre, cantidad):
    nuevo_producto = Producto(nombre=nombre, cantidad=cantidad)
    db.session.add(nuevo_producto)
    db.session.commit()
    
    json_retornado = {
            'ID': nuevo_producto.id,
            'Nombre': nuevo_producto.nombre,
            'Cantidad': nuevo_producto.cantidad
    }
    
    return json_retornado