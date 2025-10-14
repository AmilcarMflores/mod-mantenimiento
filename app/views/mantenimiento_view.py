from flask import render_template, url_for
from flask_login import current_user

def crear_ticket():
    return render_template(
        "crear.html",
        title="Crear ticket",
        current_user=current_user
        users=users,
    )

def list_ticket(tickets):
    return render_template(
        "base.html",
        tickets=tickets,
        title="Lista de tickets",
        current_user=current_user,
    )

def update_ticket_ini(ticket):
    return render_template(
        "actualizar_ini.html",
        title="Actualizar ticket",
        ticket=ticket,
        current_user=current_user,
    )

def update_ticket_fin(ticket):
    return render_template(
        "actualizar_fin.html",
        title="Actualizar ticket fin",
        ticket=ticket,
        current_user=current_user,
    )

def generate_ticket(ticket):
    return render_template(
        "generate_ticket.html",
        title="Ticket",
        ticket=ticket,
        current_user=current_user,
        download_url=url_for('ticket.download_report')
    )