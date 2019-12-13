from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core aplicacion_demo."""
    app = Flask(__name__, instance_relative_config=False,
                template_folder="../templates")
    db.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from . import modelos
        from . import rutas_inicio
        from . import rutas_cliente
        from . import rutas_tarjetas
        from . import rutas_ventas

        # Create tables for our models
        db.create_all()

        return app