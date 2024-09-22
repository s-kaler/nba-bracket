import sqlite3

CONN = sqlite3.connect('music_library.db')
CURSOR = CONN.cursor()
