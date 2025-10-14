from flask import Flask
from controllers import mantenimiento_controller
from database import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mantenimiento.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "clave-secreta-super-segura-cambiar-en-produccion"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Crear directorio de uploads si no existe
UPLOAD_FOLDER = os.path.join('static', 'uploads', 'evidencias')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)
app.register_blueprint(mantenimiento_controller.mantenimiento_bp)

with app.app_context():
    db.create_all()
    print("✓ Base de datos y tablas creadas correctamente.")

if __name__ == "__main__":
    app.run(debug=True)