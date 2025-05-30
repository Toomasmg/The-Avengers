from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from routes.avengers import avenger_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "vinificacion-secreta"

    db.init_app(app)
    
    app.register_blueprint(avenger_bp)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
