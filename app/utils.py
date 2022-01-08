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
    lg_id = session['lg']
    lg = db.session.query(Idlogin).get(lg_id)
    if lg is None:
        it_is = False
    return it_is

    