from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f'<Usuario es {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    #Este metodo va a acceder a la clase en si, y buscará un usuario por su email
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    #Este metodo va a guardar en la DB el usuario creado
    def save(self):
        db.session.add(self)
        db.session.commit()

    #Este metodo va a borrar de la DB el usuario creado
    def delete(self):
        db.session.delete(self)
        db.session.commit()