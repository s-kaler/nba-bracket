# lib/models/artist.py
from models.__init__ import CURSOR, CONN


class Artist:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, genre, id=None):
        self.id = id
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}, Genre: {self.genre}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError(
                "Genre must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Artist instances """
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Artist instances """
        sql = """
            DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and genre values of the current Artist instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO artists (name, genre)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.genre))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, genre):
        """ Initialize a new Artist instance and save the object to the database """
        artist = cls(name, genre)
        artist.save()
        return artist
    
    def update(self):
        """Update the table row corresponding to the current Artist instance."""
        sql = """
            UPDATE artists
            SET name = ?, genre = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.genre, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Artist instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM artists
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return an artist object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        artist = cls.all.get(row[0])
        if artist:
            # ensure attributes match row values in case local instance was modified
            artist.name = row[1]
            artist.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            artist = cls(row[1], row[2])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist

    @classmethod
    def get_all(cls):
        """Return a list containing an artist object per row in the table"""
        sql = """
            SELECT *
            FROM artists
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return an artist object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return an artist object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM artists
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def albums(self):
        """Return list of employees associated with current artist"""
        from models.album import Album
        sql = """
            SELECT * FROM albums
            WHERE artist_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Album.instance_from_db(row) for row in rows
        ]