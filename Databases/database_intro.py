
### Challenge #1 (Drinks: python dicts): 
# How many drinks do you need to buy to throw a great party? 
# you will have a list of your friends, and their favorite drink. 
# you will also know how many drinks of a certain type are drunk per hour


#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}


#types of drinks people drink, with lists of examples
cocktails = ['gin and tonic', 'mate vodka', 'rum and coke']

wines = ['red wine', 'white wine']

liquors = ['whiskey', 'gin', 'vokda']

nonalcoholic = ['tea', 'water', 'orange juice']

# number of drinks per hour people drink, depeneding on the type. 
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3, 'wines':2, 'liquors':2, 'nonalcoholic':3}

print("This is a calculator for your Party, to calculate how many drinks you need. ")
hours = int(input("How long will the party be?  ->"))

def drinks_calc():

	cocktail_counter = 0
	wine_counter = 0
	liquour_counter = 0 
	nonalcoholic_counter = 0
	beer_counter = 0

	for key, value in favorite_drinks.items():
		if value.lower() in cocktails:
			cocktail_counter += 1 * number_of_drinks_per_hour_per_type['cocktails'] * hours

		elif value.lower() in wines:
			wine_counter += 1 * number_of_drinks_per_hour_per_type['wines'] * hours

		elif value.lower() in liquors:
			liquour_counter += 1 * number_of_drinks_per_hour_per_type['liquors'] * hours

		elif value.lower() in nonalcoholic:
			nonalcoholic_counter += 1 * number_of_drinks_per_hour_per_type['nonalcoholic'] * hours

		elif value.lower() == 'beer':
			beer_counter += 1 * number_of_drinks_per_hour_per_type['beers'] * hours

		else:
			print(value) 

		total_drinks = cocktail_counter + beer_counter + wine_counter + liquour_counter + nonalcoholic_counter

		
	print("Cocktails: ",cocktail_counter,"\n" "  Beers: ", beer_counter,"\n" "  Wines: ", wine_counter,"\n" "  Liquors: ", liquour_counter,"\n" "  Nonalcoholics:", nonalcoholic_counter)
	print("----------")
	print("Total: ",total_drinks)
	
drinks_calc()

