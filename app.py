from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from routes.avengers import avenger_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos usando variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "tangamandapio"

    # Inicializar la base de datos
    db.init_app(app)

    # Crear tablas si no existen (se debe hacer dentro del contexto)
    with app.app_context():
        db.create_all()

    # Registrar blueprint para rutas de Avengers
    app.register_blueprint(avenger_bp)

    # Ruta principal (index)
    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
