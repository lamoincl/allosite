import enum
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship
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
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

Base = declarative_base()


class Allo(Base):
    __tablename__ = 'allo'

    allo_id = db.Column(db.Integer, primary_key=True)
    allo_nom = db.Column(db.String(50))
    allo_heure = db.Column(db.String(30))
    est_gratuit = db.Column(db.Boolean, default=True)

    commande = relationship("Commande", back_populates="allo")


class StatusEnum(enum.Enum):
    ENVOYE = "envoyé"
    PAYE = "payé"
    PREPARATION = "en préparation"
    LIVRAISON = "en cours de livraison"
    LIVRE = "livré"

    EXTE = "en exté"
    MEUH = "à la meuh"


class Commande(Base):
    __tablename__ = 'commande'

    cmd_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.ENVOYE)
    lieu = db.Column(db.Enum(StatusEnum), default=StatusEnum.MEUH)
    id_fb = db.Column(db.String(50))
    appart = db.Column(db.String(3), nullable=True)
    adress = db.Column(db.String(150), nullable=True)
    com = db.Column(db.String(300), default="")
    cmd_date = db.Column(db.DateTime())

    allo_id = db.Column(db.Integer, ForeignKey('allo.allo_id', ondelete="CASCADE"))
    allo = relationship("Allo", back_populates="commande")


class Idlogin(Base):
    __tablename__ = 'idlogin'

    login_id = db.Column(db.Integer, primary_key=True)
    login_date = db.Column(db.DateTime())


Base.metadata.create_all(engine)
