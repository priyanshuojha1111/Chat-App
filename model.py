import sqlite3 as sql
from os import path
from datetime import datetime

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "database.db")

if not path.exists(db_path):
	con = sql.connect(db_path)
	cursor = con.cursor()
	query = """
		CREATE TABLE posts (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			post TEXT NOT NULL,
			datetime TIMESTAMP
			);
		"""
	cursor.execute(query)
	

	query = """
		CREATE TABLE credentials (
			username TEXT NOT NULL PRIMARY KEY,
			userpass TEXT NOT NULL
		);
	"""
	cursor.execute(query);
	con.close()

def create_post(name, content, time):
	con = sql.connect(db_path)
	cursor = con.cursor()
	query = """
		INSERT INTO posts (name, post, datetime) values (?, ?, ?);
	"""
	cursor.execute(query, (name, content, time))
	con.commit()
	con.close()
	
def fetch_posts():
	con = sql.connect(db_path)
	cursor = con.cursor()
	query = """
		SELECT * FROM posts;
	"""
	cursor.execute(query)
	posts = cursor.fetchall()
	con.close()
	return posts

def register_user(username, userpass):
	con = sql.connect(db_path)
	cursor = con.cursor()
	query = """
		INSERT INTO credentials (username, userpass) values (?, ?);
	"""
	cursor.execute(query, (username, userpass))
	con.commit()
	con.close()

def authenticate_user(username, userpass):
	con = sql.connect(db_path)
	cursor = con.cursor()
	query = """
		SELECT * from credentials where username = ? and userpass = ?;
	"""
	cursor.execute(query, (username, userpass))
	rows = cursor.fetchall()
	if rows:
		return True

	return False