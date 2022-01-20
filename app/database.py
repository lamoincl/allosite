import enum
import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, ARRAY, Enum, PickleType, Float, Boolean, Time
from sqlalchemy.orm import declarative_base, relationship, backref

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
    allo_debut = Column(Time)
    allo_fin = Column(Time)
    se_reserve = db.Column(db.Boolean, default=True)

    commande = relationship("Commande", back_populates="allo")


class StatusEnum(enum.Enum):
    ENVOYE = "envoyé"
    PAYE = "payé"
    PREPARATION = "en préparation"
    LIVRAISON = "en cours de livraison"
    LIVRE = "livré"
    ANNULE = "annulé"
    VALIDE = "validé"

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
    prix = Column(Float, default=0)

    allo_id = db.Column(db.Integer, ForeignKey('allo.allo_id', ondelete="CASCADE"))
    allo = relationship("Allo", back_populates="commande")


class CommandeCrepe(Base):
    __tablename__ = 'crepe'

    crepe_id = Column(Integer, primary_key=True)
    crepe_suc = Column(Integer, default=0)
    crepe_nut = Column(Integer, default=0)
    crepe_con = Column(Integer, default=0)
    crepe_nat = Column(Integer, default=0)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("crepe", uselist=False))


class CommandeSnack(Base):
    __tablename__ = 'snack'

    snack_id = Column(Integer, primary_key=True)
    snack_kebab = Column(Integer, default=0)
    snack_burger = Column(Integer, default=0)
    snack_panini = Column(Integer, default=0)
    snack_croque = Column(Integer, default=0)
    snack_fanta = Column(Integer, default=0)
    snack_coca = Column(Integer, default=0)
    snack_icetea = Column(Integer, default=0)
    snack_tropico = Column(Integer, default=0)
    snack_oasis = Column(Integer, default=0)
    snack_sevenup = Column(Integer, default=0)
    snack_sevenupm = Column(Integer, default=0)
    snack_com = Column(String(300))

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("snack", uselist=False))


class CommandeFastfood(Base):
    __tablename__ = 'fastfood'

    fastfood_id = Column(Integer, primary_key=True)
    fastfood_commande = Column(String(1000))

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("fastfood", uselist=False))


class CommandeAlcool(Base):
    __tablename__ = 'alcool'

    alcool_id = Column(Integer, primary_key=True)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("alcool", uselist=False))


class CommandeCocktail(Base):
    __tablename__ = 'cocktail'

    cocktail_id = Column(Integer, primary_key=True)
    iCoffee = Column(Integer, default=0)
    aCoffee = Column(Integer, default=0)
    lait = Column(Integer, default=0)
    jar = Column(Integer, default=0)
    vodk = Column(Integer, default=0)
    ubh = Column(Integer, default=0)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("cocktail", uselist=False))


class CommandeViennoiserie(Base):
    __tablename__ = 'viennoiserie'

    viennoiserie_id = Column(Integer, primary_key=True)
    viennoiserie_pain = Column(Boolean)
    viennoiserie_croissant = Column(Boolean)
    viennoiserie_choco = Column(Boolean)
    viennoiserie_cafe = Column(Boolean)
    viennoiserie_crepe = Column(Boolean, default=False)
    viennoiserie_jus = Column(Boolean, default=False)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("viennoiserie", uselist=False))


class CommandeCigarette(Base):
    __tablename__ = 'cigarette'

    cigarette_id = Column(Integer, primary_key=True)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("cigarette", uselist=False))


class CommandeCapote(Base):
    __tablename__ = 'capote'

    capote_id = Column(Integer, primary_key=True)
    capote_nombre = Column(Integer, default=0)

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("capote", uselist=False))


class CommandeCovoit(Base):
    __tablename__ = 'covoit'

    covoit_id = Column(Integer, primary_key=True)
    covoit_depart = Column(String(100))
    covoit_destination = Column(String(100))
    covoit_heure = Column(String(50))

    cmd_id = Column(Integer, ForeignKey('commande.cmd_id'))
    cmd = relationship("Commande", backref=backref("covoit", uselist=False))


class Idlogin(Base):
    __tablename__ = 'idlogin'

    login_id = db.Column(db.Integer, primary_key=True)
    login_date = db.Column(db.DateTime())
