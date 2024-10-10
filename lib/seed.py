#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.team import Team
from models.player import Player

def seed_database():
    Team.drop_table()
    Team.create_table()
    Player.drop_table()
    Player.create_table()

    
seed_database()
print("Seeded database")