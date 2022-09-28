import pandas as pd
from flask import Flask, render_template
import sqlite3
import os #allows us to have access to the underlying operating system

# create a new flask app
app = Flask(__name__)

# create a function that will be called when the user accesses the root of the website
def get_db_connection():
    dir = os.getcwd() + '/patients.db' ##we bring the os. because flask sometimes gets confused as to where the files are
    #so we indicate os.getcwd (current working directory)
    print('dir:', dir) #do a print command to make sure its looking into the right folder
    conn = sqlite3.connect(dir) # create a connection to the database
    conn.row_factory = sqlite3.Row # The line of code assigning sqlite3.Row to the row_factory of connection creates a 'dictionary cursor', - instead of tuples it starts returning 'dictionary' rows after fetchall or fetchone
    # for more information about it look on stackoverflow: https://stackoverflow.com/questions/44009452/what-is-the-purpose-of-the-row-factory-method-of-an-sqlite3-connection-object
    return conn

@app.route('/') #using html
def index():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql:', patientListSql)
    return render_template('index.html', listPatients=patientListSql) 

@app.route('/bootstrap')
def bootstrap():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('bootstrap_example.html', listPatients=patientListSql) # note, these are two variables, patientsList is what we can then look up in the .html, and the patientsListSql is the actual data we are pulling from the sqlite db


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


