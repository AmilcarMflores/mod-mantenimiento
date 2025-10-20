from flask import Flask, redirect, url_for
from flask_socketio import SocketIO
from controllers import mantenimiento_controller, chat_controller
from database import db
from socket_events import register_socket_events
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mantenimiento.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "clave-secreta-super-segura-cambiar-en-produccion"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Inicializar Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*")

# Crear directorio de uploads si no existe
UPLOAD_FOLDER = os.path.join('static', 'uploads', 'evidencias')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)

# Registrar blueprints
app.register_blueprint(mantenimiento_controller.mantenimiento_bp)
app.register_blueprint(chat_controller.chat_bp)

# Registrar eventos de Socket.IO
register_socket_events(socketio)

# Ruta raíz que redirige a la lista de mantenimientos
@app.route("/")
def index():
    return redirect(url_for("mantenimiento.list_mantenimiento"))

with app.app_context():
    db.create_all()
    print("\n" + "="*60)
    print("✓ Base de datos y tablas creadas correctamente.")
    print("✓ Servidor corriendo en: http://127.0.0.1:5000")
    print("="*60)
    print("\n📋 RUTAS DISPONIBLES:")
    print("   🏠 Inicio:          http://127.0.0.1:5000/")
    print("   📝 Lista tickets:   http://127.0.0.1:5000/mantenimiento")
    print("   ➕ Crear ticket:    http://127.0.0.1:5000/mantenimiento/crear")
    print("   💬 Chat:            http://127.0.0.1:5000/chat")
    print("   🔔 Notificaciones:  http://127.0.0.1:5000/notificaciones")
    print("="*60 + "\n")

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)