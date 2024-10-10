# lib/models/team.py
from models.__init__ import CURSOR, CONN
from models.team import Team


class Player:
    all = {}
    def __init__(self, name, height, position, starter, team_id=None, id=None):
        self.name = name
        self.height = height
        self.position = position
        self.team_id = team_id
        self.starter = starter
        self.id = id

    def __repr__(self):
        height_formatted = f"{int(self.height / 12)}\'{self.height % 12}\""
        return f"{self.name}: {height_formatted}, {self.position}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "name must be a non-empty string"
            )
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if isinstance(height, (int)) and height > 0:
            self._height = height
        else:
            raise ValueError(
                "height must be a positive number"
            )
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        if isinstance(position, str) and len(position):
            self._position = position
        else:
            raise ValueError(
                "position must be a non-empty string"
            )
        
    @property
    def starter(self):
        return self._starter
    
    @starter.setter
    def starter(self, starter):
        if isinstance(starter, int) and (starter == 0 or starter == 1):
            self._starter = starter
        else:
            raise ValueError(
                "starter must be a 0 or 1"
            )
        
    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        if isinstance(team_id, int) and Team.find_by_id(team_id):
            self._team_id = team_id
        elif team_id is None:
            self._team_id = None
        else:
            raise ValueError(
                "team_id must reference a team in the database or None")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            height INTEGER,
            position TEXT,
            starter BIT,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO players (name, height, position, starter, team_id)
                VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.height, self.position, self.starter, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE players
            SET name = ?, height = ?, position = ?, starter = ?, team_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.height, self.position, self.starter, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, height, position, starter, team_id):
        player = cls(name, height, position, starter, team_id) 
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for  existing instance using the row's primary key
        player = cls.all.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.name = row[1]
            player.height = row[2]
            player.position = row[3]
            player.starter = row[4]
            player.team_id = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1], row[2], row[3], row[4], row[5])
            player.id = row[0]
            cls.all[player.id] = player
        return player


    @classmethod
    def get_all(cls):
        """Return a list containing one player object per table row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return player object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_height(cls, height):
        """Return list of player objects corresponding to all table rows matching specified height"""
        sql = """
            SELECT *
            FROM players
            WHERE height is ?
        """

        rows = CURSOR.execute(sql, (height,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_position(cls, position):
        """Return list of player objects corresponding to all table rows matching specified position"""
        sql = """
            SELECT *
            FROM players
            WHERE
                position LIKE ?
        """

        rows = CURSOR.execute(sql, (f"%{position}%",)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_starter(cls, starter):
        """Return list of player objects corresponding to all table rows matching specified starter status"""
        sql = """
            SELECT *
            FROM players
            WHERE starter is ?
        """

        rows = CURSOR.execute(sql, (starter,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def find_by_team_id(cls, team_id):
        """Return list of player objects corresponding to all table rows matching specified team id"""
        sql = """
            SELECT *
            FROM players
            WHERE team_id is ?
        """

        rows = CURSOR.execute(sql, (team_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_starter_and_team(cls, starter, team_id):
        """Return list of player objects corresponding to all table rows matching specified starter and team id"""
        sql = """
            SELECT *
            FROM players
            WHERE starter is ? AND team_id is ?
        """

        rows = CURSOR.execute(sql, (starter, team_id)).fetchall()
        return [cls.instance_from_db(row) for row in rows]