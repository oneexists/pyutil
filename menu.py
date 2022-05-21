#!/usr/bin/env python3
from datetime import datetime
from models import Book, Quote, Album

options = {
    1: 'Add Quote',
    2: 'Random Quote',
    3: 'All Albums',
	4: 'Add Album',
	5: 'Add Book',
	6: 'Exit'
}

def datetime_now():
	return datetime.now().strftime('%Y-%m-%d')

def print_menu():
	for key, value in options.items():
		print (str(key) + " - " + value)

def add_book():
	print("Separate multiple authors with a semicolon and no spaces.")
	new_title = input("Book title: ")
	new_authors = input("Book authors: ")
	new_language = input("Language: ")
	new_pages = input("Pages: ")
	new_start = input("Start date: ")
	new_finish = input("Finish date: ")
	new_book = Book(title = new_title, author = new_authors, language = new_language, pages = new_pages, started = new_start, finished = new_finish, created = datetime_now(), updated = datetime_now())
	new_book.save_book()

def add_quote():
	new_quote_text = input('Quote: ')
	new_citation = input('Citation: ')
	new_quote = Quote(quote_text = new_quote_text, citation = new_citation, created = datetime_now(), updated = datetime_now())
	new_quote.save_quote()

def random_quote():
	print(Quote.random_quote())

def add_album():
	print("Separate multiple artists and languages with a semicolon and no spaces.")
	new_title = input('Album title: ')
	new_artists = input('Artists: ')
	new_languages = input('Languages: ')
	new_album = Album(title = new_title, artists = new_artists, languages1 = new_languages, created = datetime_now(), updated = datetime_now())
	new_album.save_album()

def all_albums():
	print(Album.all_albums())

def main():
	while(True):
		print_menu()
		selection = input('Enter selection: ')
		try:
			selection = int(selection)
		except ValueError:
			print(f"{selection} is not a valid choice. Please select from menu choices.")

		if selection == 1:
			add_quote()
		elif selection == 2:
			random_quote()
		elif selection == 3:
			all_albums()
		elif selection == 4:
			add_album()
		elif selection == 5:
			add_book()
		elif selection == 6:
			print('Exiting application.')
			exit()
		elif isinstance(selection, int):
			print(f"{selection} is not a valid choice. Please select from menu choices.")


if __name__ == '__main__': 
		main()
