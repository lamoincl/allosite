import datetime

from database import Base, engine, db, Allo

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

allos = [
    {'allo_id': 1, 'allo_nom': 'Allô crêpe', 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': False},
    {'allo_id': 2, 'allo_nom': "Allô snack", 'allo_debut': datetime.time(8), 'allo_fin': datetime.time(20), 'se_reserve': True},
    {'allo_id': 3, 'allo_nom': "Allô fastfood", 'allo_debut': datetime.time(8), 'allo_fin': datetime.time(20), 'se_reserve': True},
    {'allo_id': 4, 'allo_nom': 'Allô cocktail', 'allo_debut': datetime.time(20), 'allo_fin': datetime.time(1), 'se_reserve': False},
    {'allo_id': 5, 'allo_nom': "Allô petit dej'", 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': True},
    {'allo_id': 6, 'allo_nom': "Allô capotes", 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(1), 'se_reserve': False},
    {'allo_id': 7, 'allo_nom': 'Allô covoit', 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': True},
    {'allo_id': 8, 'allo_nom': 'Allô vaisselle', 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 9, 'allo_nom': "Allô cendrillon", 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 10, 'allo_nom': 'Allô lessive', 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(3), 'se_reserve': True},
    {'allo_id': 11, 'allo_nom': 'Allô poubelle', 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 12, 'allo_nom': 'Allô facteur', 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 13, 'allo_nom': "Allô'rondanse", 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 14, 'allo_nom': 'Allô cornemuse', 'allo_debut': datetime.time(18), 'allo_fin': datetime.time(22), 'se_reserve': False},
    {'allo_id': 15, 'allo_nom': 'Allô président', 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': False},
    {'allo_id': 16, 'allo_nom': 'Allô shifumi', 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': False},
    {'allo_id': 17, 'allo_nom': 'Allô UNO', 'allo_debut': datetime.time(20), 'allo_fin': datetime.time(0), 'se_reserve': False},
    {'allo_id': 18, 'allo_nom': 'Allô la terre ici ma lune', 'allo_debut': datetime.time.min, 'allo_fin': datetime.time.max, 'se_reserve': False},
    {'allo_id': 19, 'allo_nom': "Allô à l'eau", 'allo_debut': datetime.time(20), 'allo_fin': datetime.time(0), 'se_reserve': False},
]

for allo in allos:
    new_allo = Allo(**allo)
    db.session.add(new_allo)

db.session.commit()
