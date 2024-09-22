#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.album import Album

def seed_database():
    Artist.drop_table()
    Album.drop_table()
    Artist.create_table()
    Album.create_table()

    """
    # Create seed data
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)
    """
    


seed_database()
print("Seeded database")
