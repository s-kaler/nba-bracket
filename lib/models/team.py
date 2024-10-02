# lib/models/team.py
from models.__init__ import CURSOR, CONN
from models.pokemon import Pokemon


class Team:
    all = {}
    def __init__(self, nickname, pokemon_id, in_party=True, id=None):
        self.nickname = nickname
        self.pokemon_id = pokemon_id
        self.in_party = in_party
        self.id = id

    def __repr__(self):
        pokemon = Pokemon.find_by_id(self.pokemon_id)
        if self.in_party:
            return f"{self.nickname} (In Party): {pokemon}"
        return f"{self.nickname}: {pokemon}"
    
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        if isinstance(nickname, str) and len(nickname):
            self._nickname = nickname
        else:
            raise ValueError(
                "Nickname must be a non-empty string"
            )
    
    @property
    def in_party(self):
        return self._in_party

    @in_party.setter
    def in_party(self, in_party):
        if isinstance(in_party, int) and in_party == 0 or in_party == 1:
            self._in_party = in_party
        else:
            raise ValueError(
                "in_party must be a 0 or 1"
            )

    @property
    def pokemon_id(self):
        return self._pokemon_id

    @pokemon_id.setter
    def pokemon_id(self, pokemon_id):
        if type(pokemon_id) is int and Pokemon.find_by_id(pokemon_id):
            self._pokemon_id = pokemon_id
        else:
            raise ValueError(
                "pokemon_id must reference a pokemon in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS team (
            id INTEGER PRIMARY KEY,
            nickname TEXT,
            in_party BIT,
            pokemon_id INTEGER,
            FOREIGN KEY (pokemon_id) REFERENCES artists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists team instances """
        sql = """
            DROP TABLE IF EXISTS team;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO team (nickname, in_party, pokemon_id)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.nickname, self.in_party, self.pokemon_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE team
            SET nickname = ?, in_party = ?, pokemon_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.nickname, self.in_party, self.pokemon_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM team
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, nickname, pokemon_id, in_party):
        team = cls(nickname,pokemon_id, in_party) 
        team.save()
        return team

    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for  existing instance using the row's primary key
        team = cls.all.get(row[0])
        if team:
            # ensure attributes match row values in case local instance was modified
            team.nickname = row[1]
            team.in_party = row[2]
            team.pokemon_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            team = cls(row[1], row[2], row[3])
            team.id = row[0]
            cls.all[team.id] = team
        return team

    @classmethod
    def get_all(cls):
        """Return a list containing one team object per table row"""
        sql = """
            SELECT *
            FROM team
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return team object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM team
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_nickname(cls, nickname):
        """Return team object corresponding to first table row matching specified nickname"""
        sql = """
            SELECT *
            FROM team
            WHERE nickname is ?
        """

        row = CURSOR.execute(sql, (nickname,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_party(cls):
        """Return a list containing an artist object per row in the table matching genre attribute"""
        sql = """
            SELECT *
            FROM team
            WHERE in_party is 1
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]