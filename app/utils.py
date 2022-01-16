import datetime

from flask import session

from database import db, Idlogin
from random import seed, randint

specifique = range(1, 10)
specifique_template = (
    'crepe.html', 'snack.html', 'fastfood.html', 'alcool.html', 'cocktail.html', 'viennoiseries.html',
    'ciguarette.html', 'capotes.html', 'covoit.html'
)
ravitaillement = range(1, 9)
service = range(9, 15)
festif = range(15, 17)
jeux = range(17, 20)
egnimatique = range(20, 22)


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


def is_standard(allo_id):
    test = False
    if allo_id in standard:
        test = True
    return test


def is_quantitatif(allo_id):
    test = False
    if allo_id in quantitatif:
        test = True
    return test
