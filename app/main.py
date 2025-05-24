from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database="mydb",
        user="root",
        password="root"
    )

@app.route('/add', methods=['POST'])
def add_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO test (info) VALUES (%s);",
        (request.json['data'],)
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.route('/get', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM test;")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)