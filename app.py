from flask import *

app = Flask(__name__)


@app.route('/')
def accueil():
    context = {"sitename": ""}
    return render_template('base.html')


@app.route('/allos')
def allos():
    return render_template('allos/allos.html')


@app.route('/allos/allo-crepe')
def allo_crepe():
    return render_template('allos/allocrepe.html')


@app.route('/allos/allo-la-terre-ici-ma-lune')
def allo_la_terre_ici_ma_lune():
    return render_template('allos/allolaterreicimalune.html')


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')


if __name__ == '__main__':
    app.run()
