# api.py
from flask import Flask, request, jsonify
import sqlite3

DB_PATH = "company.db"
app = Flask(__name__)

def query_db(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows

@app.route("/get_sales", methods=["GET"])
def get_sales():
    client_id = request.args.get("client_id")
    status = request.args.get("status")
    query = "SELECT * FROM sales WHERE 1=1"
    params = []
    if client_id:
        query += " AND client_id=?"
        params.append(client_id)
    if status:
        query += " AND status=?"
        params.append(status)
    return jsonify(query_db(query, params))

@app.route("/get_purchases", methods=["GET"])
def get_purchases():
    vendor_id = request.args.get("vendor_id")
    status = request.args.get("status")
    query = "SELECT * FROM purchases WHERE 1=1"
    params = []
    if vendor_id:
        query += " AND vendor_id=?"
        params.append(vendor_id)
    if status:
        query += " AND status=?"
        params.append(status)
    return jsonify(query_db(query, params))

if __name__ == "__main__":
    app.run(debug=True)
