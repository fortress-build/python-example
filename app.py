from flask import Flask, render_template, request, redirect, url_for
from models import insert_task, get_all_tasks, conn, cursor

app = Flask(__name__)

@app.route('/')
def index():
    tasks_list = get_all_tasks()  # Get all tasks using the function in models.py
    return render_template('index.html', tasks=tasks_list)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    insert_task(title)  # Insert a new task using the function in models.py
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update_task(task_id):
    update_sql = """
    UPDATE tasks SET done = NOT done WHERE id = %s;
    """
    cursor.execute(update_sql, (task_id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    delete_sql = "DELETE FROM tasks WHERE id = %s;"
    cursor.execute(delete_sql, (task_id,))
    conn.commit()
    return redirect(url_for('index'))

# New route to view the database contents
@app.route('/view-db')
def view_db():
    tasks_list = get_all_tasks()  # Get all tasks using the function in models.py
    # Display tasks in a simple HTML table for easy viewing
    return render_template('view_db.html', tasks=tasks_list)

if __name__ == '__main__':
    app.run(debug=True)
