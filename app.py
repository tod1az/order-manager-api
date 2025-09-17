from flask import Flask
from dotenv import load_dotenv
import os
from models import db 
from routes import tasks_bp 


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

# Ruta de inicio
@app.route("/")
def home():
    return "Bienvenido a la API de Tareas con Flask"

# Obtener todas las tareas desde la base de datos

app.register_blueprint(tasks_bp)



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
