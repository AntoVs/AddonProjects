from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Each task is stored as a dictionary
tasks = []  # {'task': str, 'done': bool, 'priority': str, 'pinned': bool}

@app.route('/')
def index():
    # Pinned tasks first, then others
    sorted_tasks = sorted(tasks, key=lambda x: not x['pinned'])
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('task')
    priority = request.form.get('priority')
    if name:
        tasks.append({'task': name, 'done': False, 'priority': priority, 'pinned': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect(url_for('index'))

@app.route('/pin/<int:task_id>')
def pin_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['pinned'] = not tasks[task_id]['pinned']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

