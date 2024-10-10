# lib/models/pokemon.py
from models.__init__ import CURSOR, CONN

class Team:

    all = {
    }

    def __init__(self, name, city, league, id=None):
        self.name = name
        self.city = city
        self.league = league
        self.id = id

    def __repr__(self):
        return f"{self.city} {self.name}"

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property

    def city(self):
        return self.city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city):
            self._city = city
        else:
            raise ValueError(
                "City must be a non-empty string"
            )

    @property
    def league(self):
        return self._league

    @league.setter
    def league(self, league):
        if isinstance(league, str) and len(league):
            self._league = league
        else:
            raise ValueError(
                "League must be a non-empty string"
            )
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT,
            league TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO teams (name, city, league)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.city, self.league))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, city, league):
        team = cls(name, city, league)
        team.save()
        return team
    
    def update(self):
        sql = """
            UPDATE teams
            SET name = ?, city = ?, league = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.city, self.league, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM teams
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
        # Check the dictionary for an existing instance using the row's primary key
        team = cls.all.get(row[0])
        if team:
            # ensure attributes match row values in case local instance was modified
            team.name = row[1]
            team.city = row[2]
            team.league = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            team = cls(row[1], row[2], row[3])
            team.id = row[0]
            cls.all[team.id] = team
        return team

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM teams
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM teams
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_city(cls, city):
        sql = """
            SELECT *
            FROM teams
            WHERE city is ?
        """
        rows = CURSOR.execute(sql, (city,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_league(cls, league):
        sql = """
            SELECT *
            FROM teams
            WHERE league is ?
        """
        rows = CURSOR.execute(sql, (league,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    