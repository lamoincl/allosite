import datetime

import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, request, redirect, url_for, session
from database import db, app, Commande, Idlogin, Allo
from utils import gen_sub_id, is_logged

app.secret_key = 'P9Y44~NJmYr9rC4Ep$JE'


@app.route('/cleanup-idlogin')
def refresh_lg_id():
    print("Lancement du nettoyage de la table idlogin")
    lgs = db.session.query(Idlogin).all()
    for lg in lgs:
        delta = datetime.datetime.now() - lg.login_date
        if datetime.timedelta(seconds=14400) < delta:
            db.session.query(Idlogin).filter(Idlogin.login_id == lg.login_id).delete()
            db.session.commit()
            print("Suppression du id de login: " + str(lg.login_id))
    return "<h1>Cette page n'est accessible normalement :( !</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    wrong = 0
    if request.method == 'POST':
        if request.form['mdp'] == 'nathanderre':
            lg_id = gen_sub_id()
            session['lg'] = lg_id
            return redirect(request.args.get('next', '/'))
        else:
            wrong = 1
    return render_template('login.html', wrong=wrong)


@app.route('/')
def accueil():
    return render_template('base.html')


@app.route('/manage-commande/')
def index_manage():
    if is_logged():
        all_allos = db.session.query(Allo).all()
        return render_template('manage/index_commande.html', allos=all_allos)
    else:
        return redirect(url_for('login', next='/manage-commande'))


@app.route('/manage-commande/<allo_id>')
def manage(allo_id):
    if is_logged():
        cmds = db.session.query(Commande).filter(Commande.allo_id == allo_id).all()
        return render_template('manage/manage_commande.html', cmds=cmds)
    else:
        return redirect(url_for('login', next='/manage-commande/' + str(allo_id)))


@app.route('/suivi/<cmd_id>')
def suivi(cmd_id):
    cmd = db.session.query(Commande).get(cmd_id)
    # todo https://www.py4u.net/discuss/998590 add an auto refresh
    return render_template('suivi.html', cmd=cmd)


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

        new_cmd = Commande(id_fb=fb, appart=appart, allo_id=2)
        db.session.add(new_cmd)
        db.session.commit()
        return redirect(url_for('suivi', cmd_id=new_cmd.cmd_id))
    return render_template('allos/allolaterreicimalune.html')


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')


if __name__ == '__main__':
    app.run(debug=True)
