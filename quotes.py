import random

QUOTES_FILE = "quotes.txt"

def add_quote():
	quote = input('Quote: ')
	citation = input('Citation: ')

	print(quote + " -" + citation)
	open(QUOTES_FILE, "a").write(quote + "|" + citation + "\n")

def random_quote():
    lines = open(QUOTES_FILE).read().splitlines()
    quote = random.choice(lines)
    quote, attributed = quote.split("|")
    print(f"\n{quote}\n  - {attributed}\n")
