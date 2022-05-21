#!/usr/bin/env python3
from getpass import getpass
import random

class Book:
    def __init__(self, **kwargs):
        self._id = kwargs['id'] if 'id' in kwargs else '0000000'
        self._title = kwargs['title'] if 'title' in kwargs else 'no title'
        self._author = kwargs['author'] if 'author' in kwargs else 'no author'
        self._language = kwargs['language'] if 'language' in kwargs else 'EN'
        self._pages = kwargs['pages'] if 'pages' in kwargs else 0
        self._started = kwargs['started'] if 'started' in kwargs else None
        self._finished = kwargs['finished'] if 'finished' in kwargs else None

    @classmethod
    def books_file(cls):
        return "books.txt"

    def save_book(self):
        books_file = open(Book.books_file(), "a")
        books_file.write(f'{self.title()}|{self.author()}|{self.pages()}|{self.language()}|{self.started()}|{self.finished()}\n')
        books_file.close()

    # getter setters
    def id(self):
        return self._id

    def title(self, title = None):
        if title: self._title = title
        return self._title

    def author(self, author = None):
        if author: self._author = author
        return self._author

    def language(self, language = None):
        if language: self._language = language
        return self._language

    def pages(self, pages = None):
        if pages: self._pages = pages
        return self._pages

    def started(self, started = None):
        if started: self._started = started
        return self._started

    def finished(self, finished = None):
        if finished: self._finished = finished
        return self._finished

    def __str__(self):
        return f'Book: {self.title()} by {self.author()} [{self.language()} {self.pages()}]'


class Album:    
    def __init__(self, **kwargs):
        self._id = kwargs['id'] if 'id' in kwargs else '0000000'
        self._title = kwargs['title'] if 'title' in kwargs else None
        self._artists = kwargs ['artists'] if 'artists' in kwargs else None
        self._languages = kwargs['languages'] if 'languages' in kwargs else None

    @classmethod
    def albums_file(cls):
        return "albums.txt"

    @classmethod
    def all_albums(cls):
        album_string = ""
        album_file = open(Album.albums_file())
        lines = album_file.read().splitlines()
        for album in lines:
            album_title, album_artists, album_languages = album.split("|")
            album_artists = album_artists.split(";")
            album_languages = album_languages.split(";")
            loaded_album = Album(title = album_title, artists = album_artists, languages = album_languages)
            album_string += str(loaded_album) + "\n"
        album_file.close()
        return album_string
        
    def save_album(self):
        album_file = open(Album.albums_file(), "a")
        album_file.write(f'{self.title()}|{self.artists()}|{self.languages()}\n')
        album_file.close()

    # getter setters
    def id(self):
        return self._id

    def title(self, title = None):
        if title: self._title = title
        return self._title
    
    def artists(self, artists = None):
        if artists: self._artists = artists
        return self._artists

    def languages(self, languages = None):
        if languages: self._languages = languages
        return self._languages

    def __str__(self):
        return f'Album: {self.title()} by {self.artists()} {self.languages()}'


class Quote:

    def __init__(self, **kwargs):
        self._id = kwargs['id'] if 'id' in kwargs else '0000000'
        self._quote_text = kwargs['quote_text'] if 'quote_text' in kwargs else None
        self._citation = kwargs['citation'] if 'citation' in kwargs else None

    @classmethod
    def quotes_file(cls):
        return "quotes.txt"

    @classmethod
    def random_quote(cls):
        quote_file = open(Quote.quotes_file())
        lines = quote_file.read().splitlines()
        quote = random.choice(lines)
        quote, attributed = quote.split("|")
        random_quote = Quote(quote_text = quote, citation = attributed)
        quote_file.close()
        return str(random_quote)

    def save_quote(self):
        quote_file = open(Quote.quotes_file(), "a")
        quote_file.write(f'{self.quote_text()}|{self.citation()}\n')
        quote_file.close()
    
    # getter setters
    def id(self):
        return self._id

    def quote_text(self, quote_text = None):
        if quote_text: self._quote_text = quote_text
        return self._quote_text

    def citation(self, citation = None):
        if citation: self._citation = citation
        return self._citation

    def __str__(self):
        return f'Quote: {self.quote_text()} - {self.citation()}'
