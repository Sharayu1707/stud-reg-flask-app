from flask import Flask, render_template, request, redirect
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, email, phone, course, address) VALUES (%s,%s,%s,%s,%s)"
    values = (data['name'], data['email'], data['phone'], data['course'], data['address'])

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template('success.html')

@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(debug=True)