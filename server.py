from flask import Flask, render_template, url, request
from flask.mysqldb import MySql


#make package object instance
app=Flask()


app.config[MYSQL_HOST]='localhost'

#define routes and app logic
@app.route("/", method=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    if request.method=='POST':
        details=request.form
        firstname=details['fname']
        lastname=details['lname']

    return render_template("forms.html")


if __name__=="__main__":
    app.run(debug=True, Host="0.0.0.0", port=3000)