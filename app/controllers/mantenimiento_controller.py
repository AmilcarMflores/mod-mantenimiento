from flask import Blueprint, request, redirect, url_for, flash, Response
from flask_login import login_required, current_user
from models.mantenimiento_model import Mantenimiento
from views import mantenimiento_view
from utils.decorators import role_required
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

mantenimiento_bp = Blueprint("mantenimiento", __name__)

@mantenimiento_bp.route("/mantenimiento")
def list_mantenimiento():
    mantenimientos = Mantenimiento.get_all()
    return mantenimiento_view.list_ticket(mantenimientos)

@mantenimiento_bp.route("/mantenimiento/crear", methods=["GET", "POST"])
def create_ticket():
    if request.method == "POST":
        descripcion = request.form["descripcion"]
        prioridad = request.form["prioridad"]

        ticket = Mantenimiento(descripcion=descripcion, prioridad=prioridad)
        ticket.save()
        flash("Ticket creado correctamente.", "success")
        return redirect(url_for("mantenimiento.list_mantenimiento"))
    
    return mantenimiento_view.crear_ticket()

@mantenimiento_bp.route("/mantenimiento/actualizar_ini/<int:id>", methods=["GET", "POST"])
@role_required(['admin', 'mantenimiento'])
def update_ticket(id):
    ticket = Mantenimiento.get_by_id(id)
    if request.method == "POST":
        ticket.descripcion = request.form["descripcion"]
        ticket.prioridad = request.form["prioridad"]
        ticket.save()
        flash("Ticket actualizado correctamente.", "success")
        return redirect(url_for("mantenimiento.list_mantenimiento"))
    return mantenimiento_view.actualizar_ticket(ticket)

@mantenimiento_bp.route("/mantenimiento/actualizar_fin/<int:id>", methods=["GET", "POST"])
@role_required(['admin', 'mantenimiento'])
def update_ticket_fin(id):
    ticket = Mantenimiento.get_by_id(id)
    if request.method == "POST":
        responsable = request.form.get("responsable")
        fecha_ini_str = request.form.get("fecha_ini")
        fecha_fin_str = request.form.get("fecha_fin")
        costo_str = request.form.get("costo")
        prioridad = request.form.get("prioridad")

        fecha_ini = datetime.strptime(fecha_ini_str, "%Y-%m-%d").date() if fecha_ini_str else None
        fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date() if fecha_fin_str else None
        costo = float(costo_str) if costo_str else None

        ticket.update_mantenimiento_inicio(responsable=responsable, fecha_ini=fecha_ini, fecha_fin=fecha_fin, costo=costo, prioridad=prioridad)

        trabajo_realizado = request.form.get("trabajo_realizado") == "on"
        evidencia_url = request.form.get("evidencia_url")
        ticket.update_matenimiento_fin(trabajo_realizado=trabajo_realizado, evidencia_url=evidencia_url)

        flash("Ticket actualizado correctamente.", "success")
        return redirect(url_for("mantenimiento.list_mantenimiento"))
    return mantenimiento_view.actualizar_ticket_fin(ticket)

@mantenimiento_bp.route("/mantenimiento/delete/<int:id>", methods=["POST"])
@role_required(['admin'])
def delete_ticket(id):
    ticket = Mantenimiento.get_by_id(id)
    ticket.delete()
    flash("Ticket eliminado correctamente.", "success")
    return redirect(url_for("mantenimiento.list_mantenimiento"))

@mantenimiento_bp.route("/mantenimiento/ticket/<int:id>")
def generate_ticket(id):
    ticket = Mantenimiento.get_by_id(id)
    return mantenimiento_view.generate_ticket(ticket)

@mantenimiento_bp.route("/mantenimiento/ticket/<int:id>/download")
def download_report(id):
    ticket = Mantenimiento.get_by_id(id)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    normal_style = styles['Normal']

    elements.append(Paragraph("Reporte de Mantenimiento", title_style))
    elements.append(Paragraph(f"ID: {ticket.id_mantenimiento}", normal_style))
    elements.append(Paragraph(f"Descripción: {ticket.descripcion}", normal_style))
    elements.append(Paragraph(f"Prioridad: {ticket.prioridad}", normal_style))
    elements.append(Paragraph(f"Responsable: {ticket.responsable}", normal_style))
    elements.append(Paragraph(f"Fecha Inicio: {ticket.fecha_ini}", normal_style))
    elements.append(Paragraph(f"Fecha Fin: {ticket.fecha_fin}", normal_style))
    elements.append(Paragraph(f"Costo: {ticket.costo}", normal_style))
    elements.append(Paragraph(f"Trabajo Realizado: {'Sí' if ticket.trabajo_realizado else 'No'}", normal_style))
    elements.append(Paragraph(f"Evidencia URL: {ticket.evidencia_url}", normal_style))

    doc.build(elements)
    buffer.seek(0)

    return Response(buffer, mimetype='application/pdf', headers={"Content-Disposition": f"attachment;filename=ticket_{ticket.id_mantenimiento}.pdf"})

