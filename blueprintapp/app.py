from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    migrate.init_app(app, db)

    # IMPORTAR BLUEPRINTS
    from blueprintapp.core.routes import bp_core
    from blueprintapp.miembros.routes import bp_miembro
    from blueprintapp.tareas.routes import bp_tarea

    # REGISTRAR BLUEPRINTS
    app.register_blueprint(bp_core)

    app.register_blueprint(
        bp_miembro,
        url_prefix='/miembros'
    )

    app.register_blueprint(
        bp_tarea,
        url_prefix='/tareas'
    )

    return app