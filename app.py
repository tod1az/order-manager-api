from flask import Flask
from dotenv import load_dotenv
import os
from models.db import db 
from routes.user import users_bp
from routes.design import designs_bp
from routes.garment import garments_bp
from routes.garment_variant import garments_variant_bp 
from routes.order import orders_bp 
from extensions import bcrypt

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
bcrypt.init_app(app)

from models.item import Item

# Ruta de inicio
@app.route("/")
def home():
    return "Bienvenido a la API de gestor de ordenes"

app.register_blueprint(users_bp)
app.register_blueprint(designs_bp)
app.register_blueprint(garments_bp)
app.register_blueprint(garments_variant_bp)
app.register_blueprint(orders_bp)



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, host="0.0.0.0", port=8082)
