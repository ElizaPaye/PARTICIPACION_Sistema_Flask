from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    from blueprintapp.models_user import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_equipo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    # Blueprints
    from blueprintapp.miembros.routes import bp_miembro
    from blueprintapp.core.routes import bp_core
    from blueprintapp.tareas.routes import bp_tarea
    from blueprintapp.auth import bp_auth

    app.register_blueprint(bp_miembro, url_prefix="/miembros")
    app.register_blueprint(bp_core, url_prefix="/")
    app.register_blueprint(bp_tarea, url_prefix="/tareas")
    app.register_blueprint(bp_auth)

    with app.app_context():
        from blueprintapp.models_user import User

        print("CREANDO TABLAS...")
        db.create_all()
        print("TABLAS CREADAS")

    return app