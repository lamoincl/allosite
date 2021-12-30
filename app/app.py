import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import *

app = Flask(__name__)

# db conf
username = 'flask'
password = 'fWL1KuA3gx15OU96GcrAAzeBOTD3CMNT'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = 'db'
dbname = '/hangar'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/testdb')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'

@app.route('/')
def accueil():
    return render_template('base.html')


@app.route('/suivi')
def suivi():
    pass


@app.route('/allos')
def allos():
    return render_template('allos/allos.html')


@app.route('/allos/allo-crepe')
def allo_crepe():
    return render_template('allos/allocrepe.html')


@app.route('/allos/allo-la-terre-ici-ma-lune', methods=['GET', 'POST'])
def allo_la_terre_ici_ma_lune():
    if request.method == 'POST':
        fb = request.form['id_fb']
        appart = request.form['appart']
        print(fb, appart)
    return render_template('allos/allolaterreicimalune.html')


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')


if __name__ == '__main__':
    app.run(debug=True)
