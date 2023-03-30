from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

#make package object instance
app=Flask(__name__)


#connecting to db
def get_db_conn():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.Row
    return conn

#displaying a single name
def get_name(name_id):
    conn=get_db_conn()
    name=conn.execute('SELECT * FROM users WHERE id=?', (name_id)).fetchone()
    conn.close()
    if name is None:
        abort(404)
    return name


#define routes and app logic
@app.route("/", methods=["GET", "POST"])
def index():
    conn=get_db_conn()
    names=conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template("index.html", names=names)

@app.route("/predict")
def predict():
    return"Data Scientist, is that you?"

@app.route('/<int:name_id>')
def name(name_id):
    name=get_name(name_id)
    return render_template('names.html', name=name)



if __name__=="__main__":
    app.run(debug=True, Host="0.0.0.0", port=3000)

 


