from flask import Blueprint, render_template

bp_core = Blueprint(
    'bp_core',
    __name__,
    template_folder='templates'
)

@bp_core.route('/')
def inicio():
    return render_template('index.html')