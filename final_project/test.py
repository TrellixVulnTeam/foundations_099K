#Contact List
def contact_list():
	while True:
		print("This is a Contact List. ")
		print("You can see Contacts and add Contacts. ")
		print("For seeing Contacts type 'SEE', for adding type 'ADD'. If you want to exit, type 'EXIT'. ")

		user_command = input("Enter command here -> ")

		contacts = []

		if user_command.upper() == 'SEE':
			print(contacts)

		elif user_command.upper() == 'ADD':
			print("So you want to add a contact.")
			new_contact_name = input("Enter name here  -> ")
			new_contact_email = input("Enter Email Address  -> ")
			new_contact_phone = input("Enter phone number?  -> ")
			new_contact = [new_contact_name, new_contact_email, new_contact_phone]
			contacts.append(new_contact)

		elif user_command.upper() == 'EXIT':
			print("Exiting Contact List, thanks for using.")
			break

		else:
			print("Could not read that. Pls enter a valid command.")