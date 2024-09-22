# lib/helpers.py

from models.artist import Artist
from models.album import Album
from models.song import Song

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

#artist functions 
def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artist = Artist.find_by_name(name)
    print(artist) if artist else print(
        f'Artist {name} not found')

def find_department_by_id():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    print(artist) if artist else print(f'Artist {id_} not found')

#album functions 
def list_albums():
    albums = Album.get_all()
    for album in albums:
        print(album)


#song functions 
def list_songs():
    songs = Song.get_all()
    for song in songs:
        print(song)