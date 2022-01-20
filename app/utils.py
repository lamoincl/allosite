import ast
import datetime

from flask import session

from database import db, Idlogin, Allo
from random import seed, randint

specifique = range(1, 8)
specifique_template = (
    'crepe.html', 'snack.html', 'fastfood.html', 'cocktail.html', 'viennoiseries.html', 'capotes.html', 'covoit.html'
)
# ravitaillement = range(1, 7)
ravitaillement = [1, 3, 5, 6]
service = range(7, 13)
festif = range(13, 15)
jeux = range(15, 18)
egnimatique = range(18, 20)


def gen_sub_id():
    now = datetime.datetime.now()
    lg_id = Idlogin(login_id=int(now.strftime("%H%f")), login_date=now)
    db.session.add(lg_id)
    db.session.commit()
    return lg_id.login_id


def is_logged():
    it_is = True
    lg_id = session.get('lg', None)
    if lg_id is None:
        it_is = False
    else:
        lg = db.session.query(Idlogin).get(lg_id)
        if lg is None:
            it_is = False
    return it_is


def treve_allos():
    en_pause = False
    date = datetime.datetime.now().date()
    now = datetime.datetime.now().time()
    if date == datetime.date(2022, 1, 21):
        if datetime.time(7, 25) < now < datetime.time(18, 20):
            en_pause = True
    elif date == datetime.date(2022, 1, 24):
        if datetime.time(8, 25) < now < datetime.time(18, 20):
            en_pause = True
    elif date == datetime.date(2022, 1, 20):
        if datetime.time(8, 20) < now < datetime.time(12, 14) or datetime.time(13, 30) < now < datetime.time(17):
            en_pause = True
    elif date == datetime.date(2022, 1, 25):
        if datetime.time(9) < now < datetime.time(18, 20):
            en_pause = True
    elif date == datetime.date(2022, 1, 26):
        if datetime.time(13, 15) < now < datetime.time(18, 20):
            en_pause = True
    return en_pause


def on_est_en_weekend():
    weekend = False
    date = datetime.datetime.now().date()
    if date == datetime.date(2022, 1, 22) or date == datetime.date(2022, 1, 23):
        weekend = True
    return weekend


def est_dispo(allo):
    dispo = True
    now = datetime.datetime.now().time()

    if not allo.se_reserve:
        if treve_allos():
            dispo = False

    if allo.allo_fin < allo.allo_debut:
        if allo.allo_fin < now < allo.allo_debut:
            dispo = False
    else:
        if now < allo.allo_debut or allo.allo_fin < now:
            dispo = False

    return dispo


def set_we_hours():
    spec = (8, 9, 10, 11, 12, 14)
    allos = db.session.query(Allo).all()

    for allo in allos:
        if allo.allo_id in spec:
            if allo.allo_id == 14:
                allo.allo_debut = datetime.time(11)
                allo.allo_fin = datetime.time(22)
            elif allo.allo_id == 10:
                allo.allo_debut = datetime.time(8)
                allo.allo_fin = datetime.time(4)
            else:
                allo.allo_debut = datetime.time(8)
                allo.allo_fin = datetime.time(22)
        else:
            allo.allo_debut = datetime.time.min
            allo.allo_fin = datetime.time.max

    db.session.commit()


def set_se_hours():
    # (datetime.time(18), datetime.time(21, 30)),
    hours = (
        (datetime.time.min, datetime.time.max),
        (datetime.time(8), datetime.time(20)),
        (datetime.time(20), datetime.time(1)),
        (datetime.time.min, datetime.time.max),
        (datetime.time(18), datetime.time(1)),
        (datetime.time.min, datetime.time.max),
        (datetime.time(18), datetime.time(22)),
        (datetime.time(18), datetime.time(22)),
        (datetime.time(18), datetime.time(3)),
        (datetime.time(18), datetime.time(22)),
        (datetime.time(18), datetime.time(22)),
        (datetime.time(18), datetime.time(22)),
        (datetime.time(18), datetime.time(22)),
        (datetime.time.min, datetime.time.max),
        (datetime.time.min, datetime.time.max),
        (datetime.time(20), datetime.time(0)),
        (datetime.time.min, datetime.time.max),
        (datetime.time(20), datetime.time(0)),
    )
    allos = db.session.query(Allo).all()
    i = 0

    for allo in allos:
        allo.allo_debut = hours[i][0]
        allo.allo_fin = hours[i][1]
        i += 1

    db.session.commit()


def update_commande_list(request, cmd, html_response):
    if request.cookies.get("commandes") is not None:
        commandes = ast.literal_eval(request.cookies.get("commandes"))
        commandes.append(cmd.cmd_id)
        html_response.set_cookie('commandes', str(commandes), max_age=60 * 60 * 24 * 365)
    else:
        html_response.set_cookie('commandes', str([cmd.cmd_id]), max_age=60 * 60 * 24 * 365)
    return html_response
