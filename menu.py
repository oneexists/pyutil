#!/usr/bin/env python3
import albums
import quotes
import books

#on y va
options = {
    1: 'Add Quote',
    2: 'Random Quote',
    3: 'All Albums',
	4: 'Add Album',
	5: 'Add Book',
	6: 'Exit'
}



def print_menu():
	for key, value in options.items():
		print (str(key) + " - " + value)

def main():
	while(True):
		print_menu()
		selection = input('Enter selection: ')
		if (selection == "quote"):
			quotes.random_quote()
			exit()
		try:
			selection = int(selection)
		except ValueError:
			print(f"{selection} is not a valid choice. Please select from menu choices.")
		
		if selection == 1:
			quotes.add_quote()
		elif selection == 2:
			quotes.random_quote()
		elif selection == 3:
			albums.all_albums()
		elif selection == 4:
			albums.add_album()
		elif selection == 5:
			books.add_book()
		elif selection == 6:
			print('Exiting application.')
			exit()
		elif isinstance(selection, int):
			print(f"{selection} is not a valid choice. Please select from menu choices.")
	
		

if __name__ == '__main__': 
		main()
