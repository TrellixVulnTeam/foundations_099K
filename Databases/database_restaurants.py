		# import the python library for SQLite 
import sqlite3

# # connect to the database file, and create a connection object
# db_connection = sqlite3.connect('restaurants.db')

# # create a database cursor object, which allows us to perform SQL on the database. 
# db_cursor = db_connection.cursor()


# db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = '1'")
# kreuzberg_restaurants = db_cursor.fetchall()
	
# print("kreuzberg_restaurants contains:  ")
# print(kreuzberg_restaurants)
	
# db_connection.close()



# # connect to the database file, and create a connection object
# db_connection = sqlite3.connect('restaurants_berlin.db')

# # create a database cursor object, which allows us to perform SQL on the database. 
# db_cursor = db_connection.cursor()

# db_cursor.execute("INSERT INTO restaurants (name, neighborhood_id, price_range_id) VALUES ('Maaaah', '1', '2'), ('Asia Place', '1', '1'), ('Pasta Place', '1', '1')")
# db_connection.commit()

# db_connection.close()


# # connect to the database file, and create a connection object
# db_connection = sqlite3.connect('restaurants_berlin.db')

# # create a database cursor object, which allows us to perform SQL on the database. 
# db_cursor = db_connection.cursor()

# db_cursor.execute("INSERT INTO neighborhoods (id, name) VALUES (5, 'Friedrichshain'), (6, 'Steglitz'), (7, 'Mitte')")
# db_connection.commit()

# db_connection.close()


# # connect to the database file, and create a connection object
# db_connection = sqlite3.connect('restaurants_berlin.db')

# # create a database cursor object, which allows us to perform SQL on the database. 
# db_cursor = db_connection.cursor()

# db_cursor.execute("INSERT INTO restaurants (name, neighborhood_id, price_range_id) VALUES ('New Day', '5', '3'), ('Miseu Vong', '7', '2'), ('Die Bratpfanne', '6', '1')")
# db_connection.commit()

# db_connection.close()


# # connect to the database file, and create a connection object
# db_connection = sqlite3.connect('restaurants_berlin.db')

# # create a database cursor object, which allows us to perform SQL on the database. 
# db_cursor = db_connection.cursor()

# db_cursor.execute("CREATE TABLE people (contact_id INTEGER PRIMARY KEY, name TEXT NOT NULL, favorite_restaurant_id INTEGER NOT NULL);")
# db_connection.commit()

# db_connection.close()


# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants_berlin.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

db_cursor.execute("INSERT INTO people (name, favorite_restaurant_id) VALUES ('Lucca', '9'), ('Max', '4'), ('Adam', '1')")
db_connection.commit()

db_connection.close()