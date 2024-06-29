class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:admin1234@172.24.128.1:5432/almacen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'cac65fb88ac4b631cf7ddcba13e9cdad'
    JWT_ALGORITHM = 'HS256'