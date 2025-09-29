from flask import Flask
from dotenv import load_dotenv
import os
from models.db import db
from routes.user import users_bp
from routes.design import designs_bp
from routes.garment import garments_bp
from routes.garment_variant import garments_variant_bp
from routes.order import orders_bp
from routes.item import items_bp
from routes.auth import auth_bp
from extensions import bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)
app.url_map.strict_slashes =False


app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = True 
app.config["JWT_HTTPONLY"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
app.config["JWT_COOKIE_SAMESITE"] = "None" 

CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:5173"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
        },
    },
    supports_credentials=True,
)


jwt = JWTManager(app)
db.init_app(app)
bcrypt.init_app(app)


@app.route("/")
def home():
    return "Bienvenido a la API de gestor de ordenes"


app.register_blueprint(users_bp)
app.register_blueprint(designs_bp)
app.register_blueprint(garments_bp)
app.register_blueprint(garments_variant_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(items_bp)
app.register_blueprint(auth_bp)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0", port=8082)
