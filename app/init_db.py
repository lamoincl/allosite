from database import Base, engine, db, Allo

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

allos = [
    {'allo_nom': 'Allô crêpes', 'allo_heure': 'Toute la journée', 'est_gratuit': True},
    {'allo_nom': 'Allô la terre ici ma lune', 'allo_heure': '10h-18h', 'est_gratuit': True},
]

for allo in allos:
    new_allo = Allo(**allo)
    db.session.add(new_allo)

db.session.commit()
