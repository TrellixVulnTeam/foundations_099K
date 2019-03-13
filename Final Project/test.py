#Exercise 1

name = input("Whats your Name?  ")
age = int(input("How old are you?  "))
number_repeat = int(input("Tell me a random number...  "))

years_to_hundred = 100 - age 

print("Hey {}, you are {} years old and you will turn 100 in {} years!".format(name, age, years_to_hundred) * number_repeat + \n)



#Exercise 2
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

number = int(input("Tell me a number... "))

if number % 2 == 0:
    print("An even number!")
    if number % 4 == 0:
        print("Its an even number which is divideble by 4!")
else:
    print("an odd number!")



#Exercise 3
"""
Take a list, and write a program that prints out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that
are smaller than that number given by the user.
"""
num = int(input("Tell me a number... "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[]

for i in a:
    if i < num:
        b.append(i)

print(b)



#Exercise 4
"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""
num = int(input("Tell me a number... "))

list_even = range(1, num+1)
divider_list = []


for i in list_even:
	if num % i == 0:
		divider_list.append(i)

print(divider_list)



#Exercise 5
"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[]
for i in a:
	if i in b:
		if i not in c:
			c.append(i)
print(c)



#Excersie 6
"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
string = input("Tell me a funny Sentence... ")
string_list = string.split()

string_list_reverse = string_list[::-1]

if string_list == string_list_reverse:
	print("Woooh an palidrome sentence! (A palindrome is a string that reads the same forwards and backwards.)")
else:
	print("Its not an palidrome.")



#Exercise 7
"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]

print(b)



#Excercise 8
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""
user_one = input("Whats your name?  ")
user_two = input("Whats your name?  ")

user_one_choice = input("{} do you choose: Rock, Paper or Scissors?  ".format(user_one)).lower
user_two_choice = input("{} do you choose: Rock, Paper or Scissors?  ".format(user_two)).lower

def win(x, y):

	if x == y:
		print("Its a tie!")

	elif x == 'rock':
		if y == 'scissors':
			print("Rock wins!")
		else:
			print("Paper wins!")

	elif x == 'paper':
		if y == 'rock':
			print("Paper wins!")
		else:
			print("Scissors wins!")

	elif x == 'scissors':
		if y == 'paper':
			print("Scissors wins!")
		else:
			print("Rock wins!")

	elif x or y == 'end':
		print("End of the game.")
		break

	else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

print(win(user_one_choice, user_two_choice))



# Excercise 9
"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
"""
import random

random_number = random.randint(1, 9)
counts = 0
user_guess = 0

while user_guess != random_number and user_guess != 'exit':
    user_guess = input("Tell me ur guess... ")

    user_guess = int(user_guess)
    counts += 1

    if user_guess > random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")
    elif user_guess == 'exit':
        print("End of guessing.")
        break
    else:
        print("You guessed right!") 
        print("And it took you", counts,"tries!")



#Excersice 10
"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
except require the solution in a different way.
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists. 
Make sure your program works on two lists of different sizes. 
Write this in one line of Python using at least one list comprehension. 
(Hint: Remember list comprehensions from Exercise 7).
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [i for i in list if i == b]

#Excersice 11
"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""
num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print('prime')
		else:
			print('NOT prime')
	else:
		print('NOT prime')
	
is_prime(num)



#Excersice 12 
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""
a = [5, 10, 15, 20, 25]

def list_printer(l):
    if last > 0:
        new_list = []
        new_list.append(l[0])
        new_list.append(a[len(l) - 1])
        print(new_list)

list_printer(a)

def list_ends(l):
    return [l[0], l[len(l)-1]]



#Excercise 13
"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the 
sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def 
