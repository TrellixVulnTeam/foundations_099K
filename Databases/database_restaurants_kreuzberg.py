# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()


db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = '1'")
kreuzberg_restaurants = db_cursor.fetchall()
	
print("kreuzberg_restaurants contains:  ")
print(kreuzberg_restaurants)
	
db_connection.close()
