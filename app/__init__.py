from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # Cargar configuraciones
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Indicar dónde redirigir para login_required
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'

    # Importar modelos para que SQLAlchemy los conozca
    from . import models

    # Registrar blueprint de rutas
    from .routes import main
    app.register_blueprint(main)

    return app

