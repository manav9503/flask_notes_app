from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

def init_db():
    with sqlite3.connect('notes.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT)')
init_db()

@app.route('/')
def index():
    with sqlite3.connect('notes.db') as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('notes.db') as conn:
            conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        flash('Note added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    with sqlite3.connect('notes.db') as conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    flash('Note deleted.', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
