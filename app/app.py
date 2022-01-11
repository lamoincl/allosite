import ast
import datetime

from flask import render_template, request, redirect, url_for, session, make_response
from database import db, Commande, Idlogin, Allo, app, StatusEnum
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


@app.route('/change-status/<cmd_id>/<status>')
def change_status(cmd_id, status):
    if is_logged():
        commande = db.session.query(Commande).get(cmd_id)
        if status == 'PAYE':
            commande.status = StatusEnum.PAYE
        elif status == 'PREPARATION':
            commande.status = StatusEnum.PREPARATION
        elif status == 'LIVRAISON':
            commande.status = StatusEnum.LIVRAISON
        elif status == 'LIVRE':
            commande.status = StatusEnum.LIVRE
        db.session.commit()
    return "<h1>Cette page n'est accessible normalement :( !</h1>"


@app.route('/refresh-status/<cmd_id>')
def refresh_status(cmd_id):
    html_response = "<h1>Cette page n'est accessible normalement :( !</h1>"
    if is_logged():
        commande = db.session.query(Commande).get(cmd_id)
        html_response = render_template('refresh/manage_status.html', status=commande.status.name)
    return html_response


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


def gen_manage(allo_id, cmds):
    if is_logged():
        if cmds is None:
            cmds = db.session.query(Commande).filter(Commande.allo_id == allo_id).all()

        if request.args.get("refresh") is not None:
            html_response = render_template('refresh/manage_commande.html', cmds=cmds, allo_id=allo_id)
        else:
            html_response = render_template('manage/manage_commande.html', cmds=cmds, allo_id=allo_id)
        return html_response
    else:
        return redirect(url_for('login', next='/manage-commande/' + str(allo_id)))


@app.route('/manage-commande/<allo_id>')
def manage(allo_id):
    return gen_manage(allo_id, None)


@app.route('/manage-commande-meuh/<allo_id>')
def manage_meuh(allo_id):
    cmds = db.session.query(Commande).filter(Commande.allo_id == allo_id, Commande.lieu == StatusEnum.MEUH).all()
    return gen_manage(allo_id, cmds)


@app.route('/manage-commande-exte/<allo_id>')
def manage_exte(allo_id):
    cmds = db.session.query(Commande).filter(Commande.allo_id == allo_id, Commande.lieu == StatusEnum.EXTE).all()
    return gen_manage(allo_id, cmds)


@app.route('/suivi/<cmd_id>')
def suivi(cmd_id):
    cmd = db.session.query(Commande).get(cmd_id)
    if request.args.get("refresh") is not None:
        html_response = render_template('refresh/suivi.html', cmd=cmd)
    else:
        html_response = render_template('suivi.html', cmd=cmd)

    return html_response


@app.route('/allos')
def allos():
    all_allos = db.session.query(Allo).all()
    return render_template('allos/allos.html', allos=all_allos)


@app.route('/allos/<allo_id>', methods=['GET', 'POST'])
def allo_cmd(allo_id):
    template_name = 'allos/allocmd.html'
    html_response = render_template(template_name)

    if request.method == 'POST':
        form_values = {
            'id_fb': request.form['id_fb'],
            'cmd_date': datetime.datetime.now(),
            'com': request.form['com'],
            'allo_id': allo_id
        }
        save_mode = False

        if 'gridCheck' in request.form:
            save_mode = True
            saved_value = {'id_fb': request.form['id_fb']}

        if request.form['lieu_opt'] == 'MEUH':
            form_values['lieu'] = StatusEnum.MEUH
            form_values['appart'] = request.form['appart']
            if save_mode:
                saved_value['lieu'] = 'MEUH'
                saved_value['appart'] = request.form['appart']
        else:
            form_values['lieu'] = StatusEnum.EXTE
            form_values['adress'] = request.form['adresse']
            if save_mode:
                saved_value['lieu'] = 'EXTE'
                saved_value['adress'] = request.form['adresse']

        new_cmd = Commande(**form_values)
        db.session.add(new_cmd)
        db.session.commit()

        html_response = make_response(redirect(url_for('suivi', cmd_id=new_cmd.cmd_id)))
        if save_mode:
            html_response.set_cookie('coord_saved', str(saved_value), max_age=None)
    else:
        if request.cookies.get("coord_saved") is not None:
            coord_get = ast.literal_eval(request.cookies.get("coord_saved"))
            html_response = render_template(template_name, **coord_get)

    return html_response


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')


if __name__ == '__main__':
    app.run(debug=True)
