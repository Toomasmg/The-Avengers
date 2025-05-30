from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.avenger import Avenger
from models.database import db
import json

avenger_bp = Blueprint("avenger_bp", __name__)

# Listar todos los Avengers
@avenger_bp.route("/avengers")
def list_avengers():
    avengers = Avenger.query.all()
    return render_template("avengers/list.html", avengers=avengers)

# Mostrar formulario para agregar un nuevo Avenger
@avenger_bp.route("/avengers/new")
def new_avenger():
    return render_template("avengers/new.html")

# Crear un nuevo Avenger
@avenger_bp.route("/avengers/create", methods=["POST"])
def create_avenger():
    try:
        avenger = Avenger(
            name=request.form["name"],
            alias=request.form["alias"],
            abilities=json.dumps(request.form.getlist("abilities")),  # lista desde inputs múltiples
            actor=request.form["actor"]
        )
        db.session.add(avenger)
        db.session.commit()
        flash("Avenger agregado correctamente", "success")
        return redirect(url_for("avenger_bp.list_avengers"))
    except Exception as e:
        flash(f"Error al agregar Avenger: {e}", "danger")
        return redirect(url_for("avenger_bp.new_avenger"))

# Mostrar formulario para editar un Avenger existente
@avenger_bp.route("/avengers/edit/<string:id>")
def edit_avenger(id):
    avenger = Avenger.query.get(id)
    if not avenger:
        flash("Avenger no encontrado", "warning")
        return redirect(url_for("avenger_bp.list_avengers"))
    return render_template("avengers/edit.html", avenger=avenger)

# Actualizar los datos del Avenger
@avenger_bp.route("/avengers/update/<string:id>", methods=["POST"])
def update_avenger(id):
    avenger = Avenger.query.get(id)
    if not avenger:
        flash("Avenger no encontrado", "warning")
        return redirect(url_for("avenger_bp.list_avengers"))
    try:
        avenger.name = request.form["name"]
        avenger.alias = request.form["alias"]
        avenger.abilities = json.dumps(request.form.getlist("abilities"))
        avenger.actor = request.form["actor"]
        db.session.commit()
        flash("Avenger actualizado", "success")
    except Exception as e:
        flash(f"Error al actualizar: {e}", "danger")
    return redirect(url_for("avenger_bp.list_avengers"))

# Eliminar un Avenger
@avenger_bp.route("/avengers/delete/<string:id>")
def delete_avenger(id):
    avenger = Avenger.query.get(id)
    if avenger:
        db.session.delete(avenger)
        db.session.commit()
        flash("Avenger eliminado", "success")
    else:
        flash("Avenger no encontrado", "warning")
    return redirect(url_for("avenger_bp.list_avengers"))
