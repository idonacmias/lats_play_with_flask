import sqlite3
from flask import g
DATABASE = 'database.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)

	return db

def create_db():
	conection = sqlite3.connect(DATABASE)
	cursor = conection.cursor()
	cursor.execute("CREATE TABLE person(first_name, last_name, date_of_birth)")
	db = setattr(g)


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()



# class Cherecter:
# 	def __init__(self, name):
# 		self.name = name

if __name__ == '__main__':
	create_db()