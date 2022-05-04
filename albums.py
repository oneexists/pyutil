#!/usr/bin/env python3
ALBUMS_FILE = "album.txt"

def all_albums():
	album_file = open(ALBUMS_FILE)
	lines = album_file.read().splitlines()
	for album in lines:
		album, artists, languages = album.split("|")
		artists = artists.split(";")
		languages = languages.split(";")
		print(f"Album: {album}\tArtist: {artists}\tLanguage: {languages}")
	album_file.close()

def add_album():
	print("Separate multiple artists and languages with a semicolon and no spaces.")
	album = input("Album title: ")
	artists = input("Artists: ")
	languages = input("Language: ")
	album_file = open(ALBUMS_FILE, "a")
	album_file.write(album + "|" + artists + "|" + languages + "\n")
	album_file.close()
