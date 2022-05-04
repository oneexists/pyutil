#!/usr/bin/env python3
BOOKS_FILE = "books.txt"

def add_book():
    print("Separate multiple authors with a semicolon and no spaces.")
    title = input("Book title: ")
    author = input("Book author: ")
    pages = input("Pages: ")
    language = input("Language: ")
    start = input("Start date: ")
    finish = input("Finish date: ")
    books_file = open(BOOKS_FILE, "a")
    books_file.write(title + "|" + author + "|" + pages + "|" + language + "|" + start + "|" + finish)
    books_file.close()