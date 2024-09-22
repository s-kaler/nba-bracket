#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.album import Album
from models.song import Song

def seed_database():
    Artist.drop_table()
    Album.drop_table()
    Artist.create_table()
    Album.create_table()

    
    # Create seed data
    tame_impala = Artist.create("Tame Impala", "Altenative")
    kaytranada = Artist.create("KAYTRANADA", "Dance")
    
    currents = Album.create("Currents", 13, tame_impala.id)
    the_slow_rush = Album.create("The Slow Rush", 12, tame_impala.id)
    ninenty_nine = Album.create("99.9%", 15, kaytranada.id)
    bubba =  Album.create("BUBBA", 17, kaytranada.id)
    timeless = Album.create("TIMELESS", 21, kaytranada.id)

    #Song.create("")

    

seed_database()
print("Seeded database")
