from flask import *

app = Flask(__name__)


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
    app.run()
