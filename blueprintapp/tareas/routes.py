from flask import Blueprint
from flask import render_template_string
from flask import request
from flask import redirect

bp_tarea = Blueprint(
    'bp_tarea',
    __name__
)

tareas = []

@bp_tarea.route('/')
def index():

    html = """

<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<title>Gestión de Tareas</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

<body class="container mt-5">

<h1 class="text-center mb-4">
GESTIÓN DE TAREAS
</h1>

<form action="/tareas/agregar" method="POST" class="mb-4">

<input
type="text"
name="tarea"
placeholder="Nueva tarea"
class="form-control mb-2"
required
>

<button class="btn btn-success">
Nueva Tarea
</button>

<a href="/" class="btn btn-secondary">
Volver
</a>

</form>

<table class="table table-bordered">

<thead class="table-dark">

<tr>

<th>ID</th>
<th>Tarea</th>
<th>Estado</th>

</tr>

</thead>

<tbody>

"""

    for i, tarea in enumerate(tareas, start=1):

        html += f"""

<tr>

<td>{i}</td>
<td>{tarea}</td>
<td>Pendiente</td>

</tr>

"""

    html += """

</tbody>

</table>

</body>
</html>

"""

    return render_template_string(html)


@bp_tarea.route('/agregar', methods=['POST'])
def agregar():

    tarea = request.form['tarea']

    tareas.append(tarea)

    return redirect('/tareas')