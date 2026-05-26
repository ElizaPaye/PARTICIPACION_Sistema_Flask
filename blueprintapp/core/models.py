from blueprintapp import db

class Persona(db.Model):

    __tablename__ = 'persona'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))