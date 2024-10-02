# lib/models/pokemon.py
from models.__init__ import CURSOR, CONN

class Pokemon:

    all = {
    }

    TYPES =  [
        "Grass",
        "Fire",
        "Water",
        "Normal",
        "Electric",
        "Fighting",
        "Flying",
        "Poison",
        "Ground",
        "Rock",
        "Bug",
        "Ghost",
        "Steel",
        "Psychic",
        "Ice",
        "Dragon",
        "Dark",
        "Fairy"
    ]

    def __init__(self, name, type1, level, hp, type2=None, id=None):
        self.name = name
        self.type1 = type1
        self.level = level
        self.hp = hp
        self.type2 = type2
        self.id = id

    def __repr__(self):
        if self.type2:
            return f"{self.name}: {self.type1}/{self.type2} Type, Level {self.level}, HP: {self.hp}"
        return f"{self.name}: {self.type1} Type, Level {self.level}, HP: {self.hp}"
    
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
    def type1(self):
        return self._type

    @type1.setter
    def type1(self, type1):
        if isinstance(type1, str) and len(type1):
            if type1 in self.TYPES:
                self._type = type1
            else:
                raise ValueError(
                    "Type must be one of the existing types"
                )
        else:
            raise ValueError(
                "Type cannot be empty"
            )
        
    @property
    def type2(self):
        return self._type2

    @type2.setter
    def type2(self, type2):
        if isinstance(type2, str) and len(type2):
            if type2 in self.TYPES:
                self._type2 = type2
            else:
                raise ValueError(
                    "Type must be one of the existing types"
                )
        elif type2 == "" or type2 == None:
            self._type2 = None
        else:
            raise ValueError(
                "Type must be either empty or one of the existing types"
            )
    
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if isinstance(level, int) and (level > 0 and level <= 100):
            self._level = level
        else:
            raise ValueError(
                "Level must be an integer between 1 and 100"
            )
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and (hp > 0 and hp < 1000):
            self._hp = hp
        else:
            raise ValueError(
                "HP must be an integer between 1 and 999"
            )
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type1 TEXT,
            level INTEGER,
            hp INTEGER,
            type2 TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pokemon;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO pokemon (name, type1, level, hp, type2)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type1, self.level, self.hp, self.type2,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, type1, level, hp, type2=None):
        pokemon = cls(name, type1, level, hp, type2)
        pokemon.save()
        return pokemon
    
    def update(self):
        sql = """
            UPDATE pokemon
            SET name = ?, type1 = ?, level = ?, hp = ?, type2 = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.type1, self.level, self.hp, self.id, self.type2))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM pokemon
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
        pokemon = cls.all.get(row[0])
        if pokemon:
            # ensure attributes match row values in case local instance was modified
            pokemon.name = row[1]
            pokemon.type1 = row[2]
            pokemon.level = row[3]
            pokemon.hp = row[4]
            pokemon.type2 = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            pokemon = cls(row[1], row[2], row[3], row[4], row[5])
            pokemon.id = row[0]
            cls.all[pokemon.id] = pokemon
        return pokemon

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM pokemon
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pokemon
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return an pokemon object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM pokemon
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_type(cls, find_type):
        sql = """
            SELECT *
            FROM pokemon
            WHERE type1 is ? OR type2 is ?
        """
        rows = CURSOR.execute(sql, (find_type, find_type)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_level(cls, level):
        sql = """
            SELECT *
            FROM pokemon
            WHERE level is ?
        """
        rows = CURSOR.execute(sql, (level,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]