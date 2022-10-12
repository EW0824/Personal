
from random import randrange

keywords = {
    'Pizza': 'p',
    'Thai': 't',
    'Italian': 'i',
    'Burger': 'b',
    'Japanese': 'j',
    'Chinese': 'c',
    'Mexican': 'm',
    'Asian': 'a',
    'Greek': 'g',
    'Korean': 'k'
}


recents = "cccpbjptj"

dct = {}
for current in reversed(range(1,len(recents))):
    dct[recents[-current]] = randrange(0, 2*current)

print(dct)
print(list(keywords.keys())[list(keywords.values()).index(max(dct, key=dct.get))])
# print(keywords[keywords.values(max(dct)])