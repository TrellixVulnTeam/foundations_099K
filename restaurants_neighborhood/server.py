# A simple server using WSGI.

from wsgiref.simple_server import make_server
import sqlite3



# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')
# create a database cursor object, which allows us to perform SQL on the database.
db_cursor = db_connection.cursor()

# db_cursor.execute("SELECT * FROM restaurants WHERE neighborhood_id = '1'")
db_cursor.execute('SELECT * FROM restaurants')
all_restaurants = db_cursor.fetchall()
	

message = "<p> List of Restaurants in Kreuzberg. </p>"

for restaurant in all_restaurants:
	message += "<ul>"
	message += "<li> <strong>{}</strong> <br> Hood ID: {} <br> Price Range ID: {} </li>".format(restaurant[1], restaurant[2], restaurant[3])
	message += "</ul>"


def simple_app(_environ, start_response):
	# set status and HTTP header for response, both needed.
	status = '200 OK'
	headers = [('Content-type', 'text/html; charset=utf-8')]
	start_response(status, headers)
	# HTML body to be rendered
	body = [message.encode("utf-8")]

	return body

#define server daemon
httpd = make_server('localhost', 8000, simple_app)
print("WSGI server on port 8000...")

# server
httpd.serve_forever()


db_cursor.close()
db_connection.close()