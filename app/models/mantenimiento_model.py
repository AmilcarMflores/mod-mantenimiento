from database import db

class Mantenimiento(db.Model):
    __tablename__ = 'mantenimiento'

    id_mantenimiento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=True)
    prioridad = db.Column(db.String(50), nullable=True)

    responsable = db.Column(db.String(100), nullable=False)
    fecha_ini = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)
    costo = db.Column(db.Numeric(12, 2), nullable=False)

    trabajo_realizado = db.Column(db.Boolean, nullable=True)
    evidencia_url = db.Column(db.String(255), nullable=True)

    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.responsable = ""
        self.fecha_ini = ""
        self.fecha_fin = ""
        self.costo = 0.0
        self.trabajo_realizado = False
        self.evidencia_url = ""

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Mantenimiento.query.all()

    @staticmethod
    def get_by_id(id):
        return Mantenimiento.query.get(id)

    def update_mantenimiento_inicio(self, responsable=None, fecha_ini=None, fecha_fin=None, costo=None):
        if responsable is not None:
            self.responsable = responsable
        if fecha_ini is not None:
            self.fecha_ini = fecha_ini
        if fecha_fin is not None:
            self.fecha_fin = fecha_fin
        if costo is not None:
            self.costo = costo
        db.session.commit()

    def update_matenimiento_fin(self, trabajo_realizado=None, evidencia_url=None):
        if trabajo_realizado is not None:
            self.trabajo_realizado = trabajo_realizado
        if evidencia_url is not None:
            self.evidencia_url = evidencia_url
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    