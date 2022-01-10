import datetime

from flask import session

from database import db, Idlogin
from random import seed, randint


def gen_sub_id():
    seed(randint(0, 100))
    lg_id = Idlogin(login_id=randint(10000000, 99999999), login_date=datetime.datetime.now())
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


standard = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
quantitatif = [19, 21]


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
