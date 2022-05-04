#!/usr/bin/env python3
import random

QUOTES_FILE = "quotes.txt"

def add_quote():
    quote = input('Quote: ')
    citation = input('Citation: ')

    print(quote + " -" + citation)
    quote_file = open(QUOTES_FILE, "a")
    quote_file.write(quote + "|" + citation + "\n")
    quote_file.close()

def random_quote():
    quote_file = open(QUOTES_FILE)
    lines = quote_file.read().splitlines()
    quote = random.choice(lines)
    quote, attributed = quote.split("|")
    print(f"\n{quote}\n  - {attributed}\n")
    quote_file.close()