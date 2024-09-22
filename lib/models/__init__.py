import sqlite3

CONN = sqlite3.connect('movie_store.db')
CURSOR = CONN.cursor()
