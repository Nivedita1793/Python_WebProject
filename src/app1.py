from flask import Flask, render_template
import pathlib
import sqlite3
import pandas as pd

base_path = pathlib.Path().cwd()
db_name = "ImmigrantsDB.db"
db_path = "../database/"+db_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_fillin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    immigrantsData = cursor.execute("SELECT * FROM immigrants").fetchall()
    con.close()
    return render_template("immigrant_table_fillin.html", immigrantsData = immigrantsData)



if __name__=="__main__":
    app.run(debug=True, port=6080)