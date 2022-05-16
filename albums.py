#!/usr/bin/env python3
ALBUMS_FILE = "album.txt"

class Album:
	def __init__(self, title, artists, languages):
		self.title = title
		self.artists = artists
		self.languages = languages

	def __str__(self):
		artist_string = ' '.join(str(artist) for artist in self.artists)
		language_string = ' '.join(str(language) for language in self.languages)
		return f"{self.title} by {artist_string} {language_string}"

def all_albums():
	album_file = open(ALBUMS_FILE)
	lines = album_file.read().splitlines()
	for album in lines:
		album, artists, languages = album.split("|")
		artists = artists.split(";")
		languages = languages.split(";")
		print(Album(album, artists, languages))
	album_file.close()

def add_album():
	print("Separate multiple artists and languages with a semicolon and no spaces.")
	album = input("Album title: ")
	artists = input("Artists: ")
	languages = input("Language: ")
	album_file = open(ALBUMS_FILE, "a")
	album_file.write(album + "|" + artists + "|" + languages + "\n")
	album_file.close()
