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

def find_artist_by_id():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    print(artist) if artist else print(f'Artist {id_} not found')


def create_artist():
    name = input("Enter the artist's name: ")
    genre = input("Enter the artist's genre: ")
    try:
        artist = Artist.create(name, genre)
        print(f'Success: {artist}')
    except Exception as exc:
        print("Error creating artist: ", exc)

def update_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        try:
            name = input("Enter the artist's new name: ")
            artist.name = name
            genre = input("Enter the artist's new genre: ")
            artist.genre = genre

            artist.update()
            print(f'Success: {artist}')
        except Exception as exc:
            print("Error updating artist: ", exc)
    else:
        print(f'Artist {id_} not found')

def delete_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        artist.delete()
        print(f'Artist {id_} deleted')
    else:
        print(f'Artist {id_} not found')

def list_artists_by_genre():
    genre = input("Enter the artist's genre: ")
    if artists := Artist.find_by_genre(genre):
        for artist in artists:
            print(artist)
    else:
        print(f'No artists with {genre} found')

def artist_album_count():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        albums = artist.albums()
        if albums:
            print(f"{artist.name} has {len(albums)} albums")
        else:
            print("No albums found")
    else:
        print(f'Artist {id_} not found')

def artist_song_count():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        songs = artist.songs()
        if songs:
            print(f"{artist.name} has {len(songs)} songs")
        else:
            print("No songs found")
    else:
        print(f'Artist {id_} not found')


#album functions 
def list_albums():
    albums = Album.get_all()
    for album in albums:
        print(album)

def find_album_by_title():
    title = input("Enter the album's title: ")
    album = Album.find_by_title(title)
    print(album) if album else print(
        f'Album {title} not found')

def find_album_by_id():
    id_ = input("Enter the album's id: ")
    album = Album.find_by_id(id_)
    print(album) if album else print(f'Album {id_} not found')


def create_album():
    title = input("Enter the album's title: ")
    song_count = int(input("Enter the album's song count: "))
    artist_id = int(input("Enter the album's artist id: "))

    try:
        album = Album.create(title, song_count, artist_id)
        print(f'Success: {album}')
    except Exception as exc:
        print("Error creating album: ", exc)

def update_album():
    id_ = input("Enter the album's id: ")
    if album := Album.find_by_id(id_):
        try:
            title = input("Enter the album's new title: ")
            album.title = title
            song_count = int(input("Enter the album's new song count: "))
            album.song_count = song_count
            artist_id = int(input("Enter the album's new artist id: "))
            album.artist_id = artist_id
            album.update()
            print(f'Success: {album}')
        except Exception as exc:
            print("Error updating album: ", exc)
    else:
        print(f'Album {id_} not found')


def delete_album():
    id_ = input("Enter the album's id: ")
    if album := Album.find_by_id(id_):
        album.delete()
        print(f'Album {id_} deleted')
    else:
        print(f'Album {id_} not found')


def list_artist_albums():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        albums = artist.albums()
        for album in albums:
            print(album)
    else:
        print(f'Artist {id_} not found')
    

#song functions 
def list_songs():
    songs = Song.get_all()
    for song in songs:
        print(song)

def find_song_by_title():
    title = input("Enter the song's title: ")
    song = Song.find_by_title(title)
    print(song) if song else print(
        f'Song {title} not found')

def find_song_by_id():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    print(song) if song else print(f'Song {id_} not found')


#if trying to add song to different album, check max song count
#allow songs to have no album id, will be known as a "single"
def create_song():
    title = input("Enter the song's title: ")
    artist_id = int(input("Enter the song's artist id: "))
    album_id_text = input("Enter the song's album id: ")
    if album_id_text == '':
        album_id = None
    else:
        album_id = int(input("Enter the song's album id: "))
        album = Album.find_by_id(album_id)
    
    try:
        #if song does not have an album, it is a single
        #if creating a song, we must check if the album's song count allows for adding a new song
        #another possible approach would be that adding a song changes the album's song count
        if album_id:
            if len(album.songs()) < album.song_count:
                song = Song.create(title, artist_id, album_id)
                print(f'Success: {song}')
            else:
                print("Album already has maximum amount of songs")
        else:
            song = Song.create(title, artist_id, album_id)
            print(f'Success: {song}')
    except Exception as exc:
        print("Error creating song: ", exc)

def update_song():
    id_ = input("Enter the song's id: ")
    if song := Song.find_by_id(id_):
        try:
            title = input("Enter the song's new title: ")
            song.title = title
            artist_id = int(input("Enter the song's new artist id: "))
            song.artist_id = artist_id
            album_id = int(input("Enter the song's new album id: "))
            
            #similar to creating a new song, if there is no album id, then it is a single
            #if a song is being updated to a different album id, then we must only check if we are changing the album id
            if album_id:
                album = Album.find_by_id(album_id)
                if album_id == song.album_id:
                    song.update()
                    print(f'Success: {song}')
                else:
                    if len(album.songs()) < album.song_count:
                        song.album_id = album_id
                        song.update()
                        print(f'Success: {song}')
                    else:
                        print("Album already has maximum amount of songs")
            else:
                song.album_id = album_id
                song.update()
                print(f'Success: {song}')
                
        except Exception as exc:
            print("Error updating song: ", exc)
    else:
        print(f'Song {id_} not found')


def delete_song():
    id_ = input("Enter the song's id: ")
    if song := Song.find_by_id(id_):
        song.delete()
        print(f'Song {id_} deleted')
    else:
        print(f'Song {id_} not found')


def list_album_songs():
    id_ = input("Enter the album's id: ")
    album = Album.find_by_id(id_)
    if album:
        songs = album.songs()
        for song in songs:
            print(song)
    else:
        print(f'Album {id_} not found')
    
def list_artist_songs():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        songs = artist.songs()
        if songs:
            for song in songs:
                print(song)
        else:
            print("No songs found")
    else:
        print(f'Artist {id_} not found')

def list_artist_singles():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        songs = artist.singles()
        if songs:
            for song in songs:
                print(song)
        else:
            print("No singles found")
    else:
        print(f'Artist {id_} not found')