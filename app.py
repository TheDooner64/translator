import json
from difflib import get_close_matches


data = json.load(open('data.json', 'r'))


def print_definition(definition):
    for line in definition:
        print(line)


def translate(word):
    word = word.lower()
    capitalized_word = word.capitalize()

    definition = data.get(word)
    capitalized_definition = data.get(capitalized_word)

    if capitalized_definition:
        print_definition(capitalized_definition)
    elif definition:
        print_definition(definition)
    else:
        closest_matches = get_close_matches(word, data.keys(), n=1, cutoff=0.75)
        if len(closest_matches) > 0:
            closest_match = closest_matches[0]
            answer = input('{} was not found in the dictionary, did you mean {}? [y/n]'.format(word, closest_match))
            if answer == 'y':
                definition = data.get(closest_match)
                print_definition(definition)
        else:
            print('Nothing close to {} was found in the dictionary!'.format(word))


word = input('Enter a word: ')
translate(word)
