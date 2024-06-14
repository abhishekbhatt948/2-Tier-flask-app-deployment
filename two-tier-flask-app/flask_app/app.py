# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Set secret key
app.secret_key = '135790246810'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        sql_query = request.form['query']
        cur = mysql.connection.cursor()
        try:
            cur.execute(sql_query)
            mysql.connection.commit()
            result = cur.fetchall()
            cur.close()
            flash('Query executed successfully', 'success')
            return render_template('index.html', result=result, query=sql_query)
        except Exception as e:
            flash(str(e), 'danger')
            return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        table = request.form['table']
        values = request.form['values']
        cur = mysql.connection.cursor()
        try:
            cur.execute(f"INSERT INTO {table} VALUES ({values})")
            mysql.connection.commit()
            cur.close()
            flash('Data added successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(str(e), 'danger')
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
