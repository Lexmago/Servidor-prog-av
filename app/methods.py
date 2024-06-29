from app.extensions import db
from .models.producto import Producto
from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

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

def user_register(username, email, password):
    #Busca un usuario por su email
    user = User.get_user_by_email(email=email)

    #Si el usuario ya estaba registrado, regresamos un error
    if user is not None:
        return {'ERROR': 'Este correo ya esta registrado :( '}, 403
    
    #Se crea un objeto de tipo user con el username y el correo
    nuevo_user = User(username=username, email=email)
    nuevo_user.set_password(password=password) #A ese objeto se le setea una contraseña cifrada
    nuevo_user.save()

    return {'Nuevo usuario': {
        'username': username,
        'email': email 
        }
    }, 200 #Le damos una respuesta satisfactoria al usuario.

def login(email, password):
    user = User.get_user_by_email(email=email)
    token_caducidad = timedelta(minutes=2)

    if user and (user.check_password(password=password)):
        # Creamos un token de acceso
        token_acceso = create_access_token(identity=user.username, expires_delta=token_caducidad)
        return {'Mensaje': 'Loggeado',
                'Token': token_acceso
               }, 200
    
    return {'Error': 'Correo o contraseña no existen...'}, 400