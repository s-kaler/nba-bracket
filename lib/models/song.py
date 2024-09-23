# lib/models/song.py
from models.__init__ import CURSOR, CONN
from models.artist import Artist
from models.album import Album


class Song:

    # Dictionary of objects saved to the database.
    all = {}

    #not all songs need to be in an album
    def __init__(self, title, artist_id, album_id=None, id=None):
        self.id = id
        self.title = title
        self.album_id = album_id
        self.artist_id = artist_id

    def __repr__(self):
        return (
            f"<song {self.id}: {self.title}, " +
            f"Artist ID: {self.artist_id}>" +
            f"Album ID: {self.album_id}>"
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "title must be a non-empty string"
            )

    @property
    def artist_id(self):
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        if type(artist_id) is int and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError(
                "artist_id must reference an artist in the database")
        
    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, album_id):
        if type(album_id) is int and Album.find_by_id(album_id):
            self._album_id = album_id
        else:
            raise ValueError(
                "album_id must reference an album in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of song instances """
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist_id INTEGER,
            album_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id),
            FOREIGN KEY (album_id) REFERENCES albums(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists song instances """
        sql = """
            DROP TABLE IF EXISTS songs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, artist id, and album id values of the current song object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO songs (title, artist_id, album_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.artist_id, self.album_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current song instance."""
        sql = """
            UPDATE songs
            SET title = ?, artist_id = ?, album_id = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist_id, self.album_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current song instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM songs
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    #cannot make more songs than album song_count allows
    @classmethod
    def create(cls, title, artist_id, album_id):
        """ Initialize a new album instance and save the object to the database """
        song = cls(title, artist_id, album_id)
        song.save()
        return song

    @classmethod
    def instance_from_db(cls, row):
        """Return a Song object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        song = cls.all.get(row[0])
        if song:
            # ensure attributes match row values in case local instance was modified
            song.title = row[1]
            song.artist_id = row[2]
            song.album_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            song = cls(row[1], row[2], row[3])
            song.id = row[0]
            cls.all[song.id] = song
        return song

    @classmethod
    def get_all(cls):
        """Return a list containing one song object per table row"""
        sql = """
            SELECT *
            FROM songs
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return album object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM songs
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return album object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM songs
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None