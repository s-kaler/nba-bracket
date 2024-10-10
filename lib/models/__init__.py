import sqlite3

CONN = sqlite3.connect('nba_bracket.db')
CURSOR = CONN.cursor()
