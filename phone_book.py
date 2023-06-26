print("\n Phone Book Program\n-----------------\n")
print("1. Add a new contact\n2. Search for a contact\n3. List all contacts\n4. Exit\n")

phone_book = {}
while True:
	choice_inp = int(input("Enter your choice: "))
	if choice_inp == 1:
		name_inp = input("Enter name: ")
		phone_inp = input("Enter phone number: ")
		phone_book[name_inp] = phone_inp
		print("Contact added Successfully! \n")
	
	elif choice_inp == 2:
		name_inp = input("Enter name to search: ")
		if name_inp in phone_book:
			print("Phone number: ",phone_book.get(name_inp),"\n")
		else:
			print("The contact is not in a list \n")
	elif choice_inp == 3:
		print("Contacts \n")
		for i in phone_book:
			print(i,":",phone_book[i])
	elif choice_inp == 4:
		print("Goodbye!")
		break
	else:
		print("Wrong input\n Enter again")

