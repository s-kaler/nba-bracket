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
    Song.drop_table()
    Song.create_table()

    # Create seed data
    tame_impala = Artist.create("Tame Impala", "Alternative")
    kaytranada = Artist.create("KAYTRANADA", "Dance")
    
    currents = Album.create("Currents", 13, tame_impala.id)
    the_slow_rush = Album.create("The Slow Rush", 12, tame_impala.id)
    ninenty_nine = Album.create("99.9%", 15, kaytranada.id)
    #bubba =  Album.create("BUBBA", 17, kaytranada.id)
    #timeless = Album.create("TIMELESS", 21, kaytranada.id)

    currents_songs = [
        "Let It Happen",
        "Nangs",
        "The Moment",
        "Yes I'm Changing",
        "Eventually",
        "Gossip",
        "The Less I Know The Better",
        "Past Life",
        "Disciples",
        "'Cause I'm A Man",
        "Reality In Motion",
        "Love/Paranoia",
        "New Person, Same Old Mistakes"
    ]
    for song_title in currents_songs:
        Song.create(song_title, tame_impala.id, currents.id)

    tsr_songs = [
        "One More Year",
        "Instant Destiny",
        "Borderline",
        "Posthumous Forgiveness",
        "Breathe Deeper",
        "Tomorrow's Dust",
        "On Track",
        "Lost in Yesterday",
        "Is It True",
        "It Might Be Time",
        "Glimmer",
        "One More Hour"
    ]
    for song_title in tsr_songs:
        Song.create(song_title, tame_impala.id, the_slow_rush.id)

    ninety_songs = [
        "TRACK UNO",
        "BUS RIDE",
        "GOT IT GOOD",
        "TOGETHER",
        "DRIVE ME CRAZY",
        "WEIGHT OFF",
        "ONE TOO MANY",
        "DESPITE THE WEATHER",
        "GLOWED UP",
        "BREAKDANCE LESSON N.1",
        "YOU'RE THE ONE",
        "VIVID DREAMS",
        "LITE SPOTS",
        "LEAVE ME ALONE",
        "BULLETS"
        
    ]
    for song_title in ninety_songs:
        Song.create(song_title, kaytranada.id, ninenty_nine.id)

seed_database()
print("Seeded database")