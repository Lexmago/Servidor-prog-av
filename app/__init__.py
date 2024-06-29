# Importamos la librería Flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from .extensions import db, jwt

# Creamos una función para montar el servidor
def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Nuestra app se va a configurar desde un objeto
    db.init_app(app) #Conectamos la app con la base de datos
    jwt.init_app(app)

    with app.app_context():
        #Inicializamos la DB
        db.create_all()
        #La variable api manejará las peticiones
        api = Api(app)

        routes = APIRoutes() #Esta variable manejará las rutas
        routes.init_routes(api) #Inicializamos las rutas en nuestra API

    # Regresamos ese servidor montado
    return app