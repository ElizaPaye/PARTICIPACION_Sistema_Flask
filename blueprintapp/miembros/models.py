from blueprintapp import db

class Miembro(db.Model):

    __tablename__ = 'miembros'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    correo = db.Column(
        db.String(100),
        nullable=False
    )