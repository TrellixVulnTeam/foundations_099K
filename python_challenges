
# Python Hackerrank challenges 

#
# #
# # # Week 1
# #
#

#####################################################################################


# Challenge 1.)
# Types and Branching
"""
Given an integer, n, perform the following conditional actions:

If  n is odd, print Weird
If  n is even and in the inclusive range of 2 to 5, print Not Weird
If  n is even and in the inclusive range of 6 to 20, print Weird
If  n is even and greater than 20, print Not Weird
"""

n = int(input("Enter your Number here ->  "))

if (n in range(6, 21) or n % 2 != 0):
        print("Weird")
else:
	print("Not Weird")


#####################################################################################


# Challenge 2.)
# Number Data Types (Floats & Ints)
"""
Read two integers and print two lines. The first line should contain integer division,  
// . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.
"""

a = int(input("Enter first Number here ->  "))
b = int(input("Enter second Number here ->  "))

def divison_math(num_one, num_two):
	#prints integer divison and float divison of two numbers
	print(a // b)
	print(a / b)

divison_math(a, b)


#####################################################################################


# BONUS Challenge 2.1)
# Number Data Types (Floats & Ints)
"""
Read two integers and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""

a = int(input("Enter first Number here ->  "))
b = int(input("Enter second Number here ->  "))


def arith_oper_math(num_one, num_two):
	#prints sum, diffrence and product of two numbers
	print(num_one + num_two)
	print(num_one - num_two)
	print(num_one * num_two)

arith_oper_math(a, b)


#####################################################################################


# Challenge 3.)
# Strings (Input/Output)
"""
You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print the following:

"Hello firstname lastname! You just delved into python."
"""

a = input("Enter firstname here ->  ")
b = input("Enter lastname  here ->  ")

def full_name(first_name, last_name):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

full_name(a ,b)


-------------------------------------------------------------------------------------


# Challenge 3.1)
# String Methods: Validation
""" 
You are given a string . 
Your task is to find out if the string s contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.
"""

s = input("Enter string here ->  ")

# prints True for each string item if it contains alphanumeric characters, 
# alphabetical characters, digits, lowercase and uppercase characters 
print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))


-------------------------------------------------------------------------------------


# Challenge 3.2)
# String Methods: Alignment 
"""
You are given a partial code that is used for generating 
the HackerRank Logo of variable thickness. 
Your task is to replace the blank with rjust, ljust or center.
"""
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).______(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))


-------------------------------------------------------------------------------------


# Challenge 3.3)
# Formatting & non-base-10 counting systems 
"""
Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the
order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of n.
"""


-------------------------------------------------------------------------------------


# Challenge 3.4)
# String Methods: Join/Split
"""
You are given a string. Split the string on a " " (space) 
delimiter and join using a - hyphen.
"""

s = input("Enter String here ->  ")

def split_and_join(string):
    # write your code here
    string = string.split(" ")
    string = '-'.join(string)
    print(string)

split_and_join(s) 


-------------------------------------------------------------------------------------


# BONUS Challenge 3.5)
# String Methods: Output Alignment
"""
Read an integer n.
Without using any string methods, try to print the following:
1234...n
Note that ... represents the values in between.
"""

n = int(input("Enter number here -> "))
# *takes all positiv integers 
print(*range(1, int(n)+1), sep='')


#####################################################################################


# Challenge 4.)
#Functions and Looping (Print, multiply, loops)
"""
Read an integer n. For all non-negative integers i < n, print i**2. 
"""

n = int(input("Got a number in mind? Enter it here -> "))

for i in range(n):
    print(i**2) 


#####################################################################################


# Challenge 5.)
# Lists (Find the Runner-Up Score!)
"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
"""


-------------------------------------------------------------------------------------


# Challenge 5.1)
# Lists (Nested Lists)
"""
Given the names and grades for each student in a Physics class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.
"""


-------------------------------------------------------------------------------------


# Challenge 5.2)
# Lists (Finding the percentage)
"""
You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer n followed by the names and marks for n students. 
You are required to save the record n a dictionary data type. The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.
"""


-------------------------------------------------------------------------------------


# Challenge 5.3)
# Lists (Lists)
"""
Initialize your list and read in the value of  followed by  lines of commands where each command will
be of the  types listed above. Iterate through each command in order and perform the corresponding 
operation on your list.
"""


-------------------------------------------------------------------------------------


# Challenge 5.4)
# Lists (Tuples)
"""
Given an integer, n, and n space-separated integers as input, create a tuple, t, 
of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""



#####################################################################################

#
# #
# # # Week 2
# #
#

#####################################################################################


#Class/ Lesson Challenge 5.)
#Conditionals
"""
You are given the year, and you have to write a 
function to check if the year is leap or not.
"""

year = int(input("Enter a year here ->  "))

def is_leap(year):
    leap = False
    
	if year % 4 == 0 and year % 100 != 0:
		leap = True
	elif year % 100 == 0:
			if year % 400 == 0:
				leap = True
	elif year % 100 == 0:
		leap = False

    return leap

 #Print Function





#List Comprehension
"""
