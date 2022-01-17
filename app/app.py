import ast
import datetime

from flask import render_template, request, redirect, url_for, session, make_response
from sqlalchemy import desc

from database import db, Commande, Idlogin, Allo, app, StatusEnum, CommandeCrepe, CommandeSnack, CommandeViennoiserie, \
    CommandeFastfood, CommandeCapote, CommandeCovoit
from utils import gen_sub_id, is_logged, specifique, specifique_template, ravitaillement, service, festif, jeux, \
    egnimatique

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
        elif status == 'VALIDE':
            commande.status = StatusEnum.VALIDE
        elif status == 'ANNULE':
            commande.status = StatusEnum.ANNULE
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
        if request.args.get("refresh") is not None:
            html_response = render_template('refresh/manage_index.html', allos=all_allos, db=db, Commande=Commande, Allo=Allo, StatusEnum=StatusEnum)
        else:
            html_response = render_template('manage/index_commande.html', allos=all_allos, db=db, Commande=Commande, Allo=Allo, StatusEnum=StatusEnum)
        return html_response
    else:
        if request.args.get("refresh") is not None:
            all_allos = db.session.query(Allo).all()
            html_response = render_template('refresh/manage_index.html', allos=all_allos, db=db, Commande=Commande, Allo=Allo, StatusEnum=StatusEnum)
        else:
            html_response = redirect(url_for('login', next='/manage-commande'))
        return html_response


def gen_manage(allo_id, cmds, section):
    allo_id = int(allo_id)
    if is_logged():
        allo = db.session.query(Allo).get(allo_id)
        if request.args.get("refresh") is not None:
            if allo_id in specifique:
                html_response = render_template('manage/refresh/' + specifique_template[allo_id - 1], cmds=cmds, allo=allo, section=section)
            else:
                html_response = render_template('refresh/manage_commande.html', cmds=cmds, allo=allo, section=section)
        else:
            if allo_id in specifique:
                html_response = render_template('manage/' + specifique_template[allo_id - 1], cmds=cmds, allo=allo, section=section)
            else:
                html_response = render_template('manage/manage_commande.html', cmds=cmds, allo=allo, section=section)
        return html_response
    else:
        if request.args.get("refresh") is not None:
            allo = db.session.query(Allo).get(allo_id)
            html_response = render_template('refresh/manage_commande.html', cmds=cmds, allo=allo, section=section)
        else:
            html_response = redirect(url_for('login', next='/manage-commande/' + str(allo_id)))
        return html_response


@app.route('/manage-commande/<allo_id>')
def manage(allo_id):
    cmds = db.session.query(Commande).filter(
        Commande.allo_id == allo_id,
        Commande.status != StatusEnum.LIVRE
    ).all()
    section = 'GLOBAL'
    return gen_manage(allo_id, cmds, section)


@app.route('/manage-commande-meuh/<allo_id>')
def manage_meuh(allo_id):
    cmds = db.session.query(Commande).filter(
        Commande.allo_id == allo_id,
        Commande.lieu == StatusEnum.MEUH,
        Commande.status != StatusEnum.LIVRE
    ).all()
    section = 'MEUH'
    return gen_manage(allo_id, cmds, section)


@app.route('/manage-commande-exte/<allo_id>')
def manage_exte(allo_id):
    cmds = db.session.query(Commande).filter(
        Commande.allo_id == allo_id,
        Commande.lieu == StatusEnum.EXTE,
        Commande.status != StatusEnum.LIVRE
    ).all()
    section = 'EXTE'
    return gen_manage(allo_id, cmds, section)


@app.route('/manage-commande-livre/<allo_id>')
def manage_livre(allo_id):
    cmds = db.session.query(Commande).filter(
        Commande.allo_id == allo_id,
        Commande.status == StatusEnum.LIVRE
    ).order_by(desc(Commande.cmd_id))
    section = 'LIVRE'
    return gen_manage(allo_id, cmds, section)


@app.route('/suivi/<cmd_id>')
def suivi(cmd_id):
    cmd = db.session.query(Commande).get(cmd_id)
    allo_id = cmd.allo.allo_id
    if request.args.get("refresh") is not None:
        if allo_id in specifique:
            html_response = render_template('spec_suivi_refresh/' + specifique_template[allo_id - 1], cmd=cmd)
        else:
            html_response = render_template('refresh/suivi.html', cmd=cmd)
    else:
        if allo_id in specifique:
            html_response = render_template('spec_suivi/' + specifique_template[allo_id - 1], cmd=cmd)
        else:
            html_response = render_template('suivi.html', cmd=cmd)

    return html_response


@app.route('/allos')
def allos():
    all_allos = db.session.query(Allo).all()
    return render_template('allos/allos.html', allos=all_allos)


@app.route('/allo-groupe/<group_id>')
def allo_groupe(group_id):
    group_id = int(group_id)
    allos_grp = []

    if group_id == 1:
        for allo_id in ravitaillement:
            allos_grp.append(db.session.query(Allo).get(allo_id))
        group_name = "Besoin de te ravitailler ?"
    elif group_id == 2:
        for allo_id in service:
            allos_grp.append(db.session.query(Allo).get(allo_id))
        group_name = "Besoin d'un service ?"
    elif group_id == 3:
        for allo_id in festif:
            allos_grp.append(db.session.query(Allo).get(allo_id))
        group_name = "Besoin de plus de fête ?"
    elif group_id == 4:
        for allo_id in jeux:
            allos_grp.append(db.session.query(Allo).get(allo_id))
        group_name = "Envie de defier à un jeu la gaeliste ?"
    else:
        for allo_id in egnimatique:
            allos_grp.append(db.session.query(Allo).get(allo_id))
        group_name = "Qu'est-ce que ça peut etre ?"

    return render_template('allos/allo_group.html', allos=allos_grp, group_name=group_name)


@app.route('/allos/<allo_id>', methods=['GET', 'POST'])
def allo_cmd(allo_id):
    template_name = 'allos/allocmd.html'
    allo_id = int(allo_id)
    allo = db.session.query(Allo).get(allo_id)

    if request.method == 'POST':
        form_values = {
            'id_fb': request.form['id_fb'],
            'cmd_date': datetime.datetime.now(),
            'com': request.form['com'],
            'allo_id': allo_id
        }
        save_mode = False

        if 'prix' in request.form:
            form_values['prix'] = request.form['prix']

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

        if allo_id in specifique:
            spec_values = {'cmd_id': new_cmd.cmd_id}
            if allo_id == 1:
                spec_values['crepe_nut'] = request.form['pate']
                spec_values['crepe_con'] = request.form['confiture']
                spec_values['crepe_suc'] = request.form['sucre']
                new_spec_cmd = CommandeCrepe(**spec_values)
            elif allo_id == 2:
                spec_values['snack_kebab'] = request.form['kebab']
                spec_values['snack_burger'] = request.form['burger']
                spec_values['snack_panini'] = request.form['panini']
                spec_values['snack_croque'] = request.form['croque']
                spec_values['snack_fanta'] = request.form['FANTA']
                spec_values['snack_coca'] = request.form['COCA']
                spec_values['snack_icetea'] = request.form['ICETEA']
                spec_values['snack_tropico'] = request.form['TROPICO']
                spec_values['snack_oasis'] = request.form['OASIS']
                spec_values['snack_sevenup'] = request.form['SEVENUP']
                spec_values['snack_sevenupm'] = request.form['SEVENUPMOJITO']
                spec_values['snack_com'] = request.form['sncom']
                new_spec_cmd = CommandeSnack(**spec_values)
            elif allo_id == 3:
                spec_values['fastfood_commande'] = request.form['commande']
                new_spec_cmd = CommandeFastfood(**spec_values)
            elif allo_id == 5:
                spec_values['viennoiserie_pain'] = request.form['miam'] == "pain"
                spec_values['viennoiserie_croissant'] = request.form['miam'] == "croissant"
                spec_values['viennoiserie_choco'] = request.form['slurp'] == "choco"
                spec_values['viennoiserie_cafe'] = request.form['slurp'] == "cafe"
                new_spec_cmd = CommandeViennoiserie(**spec_values)
            elif allo_id == 6:
                spec_values['capote_nombre'] = request.form['capote']
                new_spec_cmd = CommandeCapote(**spec_values)
            elif allo_id == 7:
                spec_values['covoit_depart'] = request.form['adresse']
                spec_values['covoit_destination'] = request.form['arrive']
                spec_values['covoit_heure'] = request.form['heure']
                new_spec_cmd = CommandeCovoit(**spec_values)

            db.session.add(new_spec_cmd)
            db.session.commit()
        html_response = make_response(redirect(url_for('suivi', cmd_id=new_cmd.cmd_id)))
        if save_mode:
            html_response.set_cookie('coord_saved', str(saved_value), max_age=None)
    else:
        if allo_id in specifique:
            template_name = 'allos/' + specifique_template[allo_id - 1]

        html_response = render_template(template_name, allo=allo)

        if request.cookies.get("coord_saved") is not None:
            coord_get = ast.literal_eval(request.cookies.get("coord_saved"))
            html_response = render_template(template_name, **coord_get, allo=allo)

    return html_response


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')


@app.route('/espace-snack/<status>', methods=['GET', 'POST'])
def espace_snack(status):
    if not is_logged():
        wrong = 0
        if request.method == 'POST':
            if request.form['mdp'] == 'miaMmiAm':
                lg_id = gen_sub_id()
                session['lg'] = lg_id
                return redirect(url_for('espace_snack', status=status))
            else:
                wrong = 1
        html_response = render_template('login.html', wrong=wrong)
    else:
        if status is None:
            status = 'ENCOURS'
        if status == 'ENCOURS':
            cmds = db.session.query(Commande).filter(
                Commande.allo_id == 2,
                Commande.status != StatusEnum.LIVRE,
                Commande.status != StatusEnum.ENVOYE,
                Commande.status != StatusEnum.LIVRAISON
            ).all()
        elif status == 'TERMINE':
            cmds = db.session.query(Commande).filter(
                Commande.allo_id == 2,
                Commande.status != StatusEnum.ENVOYE,
                Commande.status != StatusEnum.PAYE,
                Commande.status != StatusEnum.PREPARATION
            ).order_by(desc(Commande.cmd_id))
        if request.args.get("refresh") is not None:
            html_response = render_template('refresh/espace-snack.html', cmds=cmds, section=status)
        else:
            html_response = render_template('espace-snack.html', cmds=cmds, section=status)
    return html_response


if __name__ == '__main__':
    app.run(debug=True)
