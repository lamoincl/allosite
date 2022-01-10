from database import Base, engine, db, Allo

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

allos = [
    {'allo_id': 1, 'allo_nom': 'Allô crêpe', 'allo_heure': 'Toute la journée', 'est_gratuit': True},
    {'allo_id': 2, 'allo_nom': 'Allô alcool', 'allo_heure': '10h-18h', 'est_gratuit': False},
    {'allo_id': 3, 'allo_nom': 'Allô cocktail', 'allo_heure': '10h-18h', 'est_gratuit': False},
    {'allo_id': 4, 'allo_nom': "Allô'rondanse", 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 5, 'allo_nom': 'Allô cornemuse', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 6, 'allo_nom': 'Allô la terre ici ma lune', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 7, 'allo_nom': "Allô à l'eau", 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 8, 'allo_nom': 'Allô UNO', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 9, 'allo_nom': 'Allô président', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 10, 'allo_nom': 'Allô shifumi', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 11, 'allo_nom': 'Allô vaisselle', 'allo_heure': 'JS: 12h-22h / WE: 8h-22h', 'est_gratuit': True},
    {'allo_id': 12, 'allo_nom': "Allô cendrillon", 'allo_heure': 'JS: 12h-22h / WE: 8h-22h', 'est_gratuit': True},
    {'allo_id': 13, 'allo_nom': 'Allô lessive', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 14, 'allo_nom': 'Allô poubelle', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 15, 'allo_nom': 'Allô facteur', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 16, 'allo_nom': 'Allô covoit', 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 17, 'allo_nom': "Allô fastfood", 'allo_heure': '10h-18h', 'est_gratuit': False},
    {'allo_id': 18, 'allo_nom': "Allô viennoiseries", 'allo_heure': '10h-18h', 'est_gratuit': False},
    {'allo_id': 19, 'allo_nom': "Allô capotes", 'allo_heure': '10h-18h', 'est_gratuit': True},
    {'allo_id': 20, 'allo_nom': "Allô snack", 'allo_heure': '10h-18h', 'est_gratuit': False},
    {'allo_id': 21, 'allo_nom': "Allô cigarette", 'allo_heure': '10h-18h', 'est_gratuit': False},
]

for allo in allos:
    new_allo = Allo(**allo)
    db.session.add(new_allo)

db.session.commit()
