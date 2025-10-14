from flask import Flask
from controllers import mantenimiento_controller
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mantenimiento.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "clave-secreta"

db.init_app(app)
app.register_blueprint(mantenimiento_controller.mantenimiento_bp)

with app.app_context():
    db.create_all()
    print("Database and tables created.")

if __name__ == "__main__":
    app.run(debug=True)
    