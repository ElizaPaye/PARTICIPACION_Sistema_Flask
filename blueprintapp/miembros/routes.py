from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from blueprintapp import db
from blueprintapp.miembros.models import Miembro

bp_miembro = Blueprint(
    'bp_miembro',
    __name__,
    template_folder='templates'
)

@bp_miembro.route('/')
def index():

    miembros = Miembro.query.all()

    return render_template(
        'miembros/index.html',
        miembros=miembros
    )


@bp_miembro.route('/agregar', methods=['POST'])
def agregar():

    nombre = request.form['nombre']
    correo = request.form['correo']

    nuevo = Miembro(
        nombre=nombre,
        correo=correo
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for('bp_miembro.index'))


@bp_miembro.route('/eliminar/<int:id>')
def eliminar(id):

    miembro = Miembro.query.get(id)

    db.session.delete(miembro)
    db.session.commit()

    return redirect(url_for('bp_miembro.index'))


@bp_miembro.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    miembro = Miembro.query.get(id)

    if request.method == 'POST':

        miembro.nombre = request.form['nombre']
        miembro.correo = request.form['correo']

        db.session.commit()

        return redirect(url_for('bp_miembro.index'))

    return render_template(
        'miembros/editar.html',
        miembro=miembro
    )