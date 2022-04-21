ALBUMS_FILE = "../trackers_db/album.txt"

def all_albums():
	lines = open(ALBUMS_FILE).read().splitlines()
	for album in lines:
		album, artists, languages = album.split("|")
		artists = artists.split(";")
		languages = languages.split(";")
		print(f"Album: {album}\tArtist: {artists}\tLanguage: {languages}")

def add_album():
	print("Separate multiple artists and languages with a semicolon and no spaces.")
	album = input("Album title: ")
	artists = input("Artists: ")
	languages = input("Language: ")
	open(ALBUMS_FILE, "a").write(album + "|" + artists + "|" + languages + "\n")

