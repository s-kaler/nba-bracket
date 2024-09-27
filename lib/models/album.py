# lib/models/album.py
from models.__init__ import CURSOR, CONN
from models.artist import Artist


class Album:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, title, song_count, artist_id, id=None):
        self.id = id
        self.title = title
        self.song_count = song_count
        self.artist_id = artist_id

    def __repr__(self):
        artist_name = Artist.find_by_id(self.artist_id).name
        return (
            f"{self.title} by {artist_name}, Tracks: {self.song_count}. " +
            f"ID: {self.id}. Artist ID: {self.artist_id}"
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
    def song_count(self):
        return self._song_count

    @song_count.setter
    def song_count(self, song_count):
        if isinstance(song_count, int) and song_count > 0:
            self._song_count = song_count
        else:
            raise ValueError(
                "song_count must be a positive int"
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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of album instances """
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT,
            song_count INTEGER,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists album instances """
        sql = """
            DROP TABLE IF EXISTS albums;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, song count, and artist id values of the current album object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO albums (title, song_count, artist_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.song_count, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current album instance."""
        sql = """
            UPDATE albums
            SET title = ?, song_count = ?, artist_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.song_count, self.artist_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current album instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM albums
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, title, song_count, artist_id):
        """ Initialize a new album instance and save the object to the database """
        album = cls(title, song_count, artist_id)
        album.save()
        return album

    @classmethod
    def instance_from_db(cls, row):
        """Return an album object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        album = cls.all.get(row[0])
        if album:
            # ensure attributes match row values in case local instance was modified
            album.title = row[1]
            album.song_count = row[2]
            album.artist_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            album = cls(row[1], row[2], row[3])
            album.id = row[0]
            cls.all[album.id] = album
        return album

    @classmethod
    def get_all(cls):
        """Return a list containing one album object per table row"""
        sql = """
            SELECT *
            FROM albums
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return album object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM albums
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return album object corresponding to first table row matching specified title"""
        sql = """
            SELECT *
            FROM albums
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def songs(self):
        """Return list of songs associated with current album"""
        from models.song import Song
        sql = """
            SELECT * FROM songs
            WHERE album_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Song.instance_from_db(row) for row in rows
        ]