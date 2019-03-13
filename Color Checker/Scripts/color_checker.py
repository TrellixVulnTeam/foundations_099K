#!/Users/lucca/AppData/Local/Programs/Python/Python37-32

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import sys
import csv

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'user_color'
# and assign it's value to a local variable called user_color
user_color = form.getvalue('color')
    
with open('colors.csv') as _filehandler:
    csv_file_reader = csv.reader(_filehandler)
    check = False
    for row in csv_file_reader:
        if user_color.title() == row[1]:
        	check = True
        	break
    if check == True:
    	print("""
    		<!DOCTYPE html>
			<html>
			<head>
			<title> Server Answer </title>
			<style>
			body {
				background: #9796f0;
			    /* fallback for old browsers */
			    background: -webkit-linear-gradient(to right, #fbc7d4, #9796f0);
			    /* Chrome 10-25, Safari 5.1-6 */
			    background: linear-gradient(to right, #fbc7d4, #9796f0);
			    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
			    text-align: center;
			    margin-top: 20em;
			    font-family: "Lucida Console", Monaco, monospace;
			}

			div.container {
				box-sizing: border-box; 
				width: 300px; 
				height: 100px; 
				padding: 30px; 
				border: 10px solid %s;
			}

			</style>
			</head>
			<body>
			<center> <div class="container">
			<div class="box">
			%s is a valid color, Hexcode: %s
			</div>
			</div>
			</center>
			</body>
			</html>
    		"""%(row[2],user_color, row[2]))

    if check == False:
    	print("""
    		<!DOCTYPE html>
			<html>
			<head>
			<title> Server Answer </title>
			<style>
			body {
				background: #9796f0;
			    /* fallback for old browsers */
			    background: -webkit-linear-gradient(to right, #fbc7d4, #9796f0);
			    /* Chrome 10-25, Safari 5.1-6 */
			    background: linear-gradient(to right, #fbc7d4, #9796f0);
			    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
			    text-align: center;
			    margin-top: 20em;
			    font-family: "Lucida Console", Monaco, monospace;
			}

			p {
				font-size: 25px;
			}

			</style>
			</head>
			<body>
			<center><p style="box-sizing: content-box; width: 300px; height: 100px; padding: 30px; border: 10px solid black;"> Not a valid one! </p> </center>
			<p style="font-size: 25px;"> %s is not a valid color! </p>
			</body>
			</html>
    		"""% user_color)