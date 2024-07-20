from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Lista de tarea 
tasks = []

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

# Ruta para agregar una nueva tarea
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

# Ruta para eliminar una tarea
@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
