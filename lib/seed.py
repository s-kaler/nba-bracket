#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.team import Team
from models.player import Player

def seed_database():
    Team.drop_table()
    Team.create_table()
    Player.drop_table()
    Player.create_table()

    teams = [
        Team("Knicks", "New York", "NBA"),
        Team("Lakers", "Los Angeles", "NBA"),
        Team("Bulls", "Chicago", "NBA"),
        Team("Spurs", "San Antonio", "NBA"),
        Team("Heat", "Miami", "NBA"),
        Team("Huskies", "UConn", "NCAA"),
        Team("Boilermakers", "Purdue", "NCAA"),
        Team("Crimson Tide", "Alabama", "NCAA"),
        Team("Cougars", "Houston", "NCAA"),
    ]
    for team in teams:
            team.save()

    knicks_roster = [
        Player("Jalen Brunson", 74, "Point Guard", 1, teams[0].id),
        Player("RJ Barrett", 79, "Small Forward", 1, teams[0].id),
        Player("Julius Randle", 81, "Power Forward", 1, teams[0].id),
        Player("Mitchell Robinson", 85, "Center", 1, teams[0].id),
        Player("Quentin Grimes", 77, "Shooting Guard", 1, teams[0].id),
        Player("Josh Hart", 75, "Shooting Guard/Small Forward", 0, teams[0].id),
        Player("Immanuel Quickley", 75, "Point Guard/Shooting Guard", 0, teams[0].id),
        Player("Isaiah Hartenstein", 84, "Center", 0, teams[0].id),
        Player("Jericho Sims", 83, "Center", 0, teams[0].id),
        Player("Louis Williams", 72, "Point Guard", 0, teams[0].id)
    ]
    for player in knicks_roster:
        player.save()

    lakers_roster = [
        Player("LeBron James", 81, "Small Forward", 1, teams[1].id),
        Player("Anthony Davis", 85, "Center", 1, teams[1].id),
        Player("D'Angelo Russell", 75, "Point Guard", 1, teams[1].id),
        Player("Lonnie Walker IV", 78, "Shooting Guard", 1, teams[1].id),
        Player("Rui Hachimura", 79, "Power Forward", 1, teams[1].id),
        Player("Dennis Schröder", 73, "Point Guard", 0, teams[1].id),
        Player("Jarred Vanderbilt", 79, "Power Forward", 0, teams[1].id),
        Player("Austin Reaves", 77, "Shooting Guard", 0, teams[1].id),
        Player("Max Christie", 79, "Small Forward", 0, teams[1].id)
    ]
    for player in lakers_roster:
        player.save()

    uconn_roster = [
        Player("Hassan Diarra", 74, "Point Guard", 1, teams[5].id),
        Player("Aidan Mahaney", 75, "Shooting Guard", 1, teams[5].id),
        Player("Jaylin Stewart", 77, "Small Forward", 1, teams[5].id),
        Player("Alex Karaban", 80, "Power Forward", 1, teams[5].id),
        Player("Samson Johnson", 83, "Center", 1, teams[5].id),
        Player("Nahiem Alleyne", 77, "Shooting Guard", 0, teams[5].id)
    ]
    for player in uconn_roster:
        player.save()

    free_agents = [
        Player("Darius Jackson", 76, "Shooting Guard/Small Forward", 0),
        Player("Andre Petrova", 74, "Point Guard", 0),
        Player("Khalil Abdul-Jabbar", 84, "Power Forward/Center", 0),
        Player("Mario Ramirez", 79, "Small Forward/Power Forward", 0),
        Player("Nikolai Ivanov", 86, "Center", 0)
    ]
    for player in free_agents:
        player.save()

        
seed_database()
print("Seeded database")