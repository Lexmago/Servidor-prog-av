# Importamos la librería Flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from .extensions import db

# Creamos una función para montar el servidor
def crear_app():
    app = Flask(__name__)
    db.init_app(app) #Aqui la DB se va a inicializar en nuestra aplicación
    app.config.from_object(Config) #Nuestra app se va a configurar desde un objeto
    api = Api(app)

    routes = APIRoutes()
    routes.init_routes(api)
    # Regresamos ese servidor montado
    return app