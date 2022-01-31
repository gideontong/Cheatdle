from os import listdir
from random import choice

DATA_FOLDER = 'data'

def return_correctness(word: str) -> tuple:
    ans = [None] * 5
    letters = list()
    not_in = set()
    for i, c in enumerate(word):
        prompt = input(f'was {c} correct (yes/misplaced/no)? ')
        if prompt == 'yes':
            ans[i] = c
        elif prompt == 'misplaced':
            letters.append(c)
        elif prompt == 'no':
            not_in.add(c)
    
    return ans, letters, not_in

def remove_possible(ans: list, letters: list, not_in: set, wordlist: list) -> list:
    for i, c in enumerate(ans):
        if c:
            for word in wordlist.copy():
                if word[i] != c:
                    wordlist.remove(word)
    
    if len(letters) > 0:
        for word in wordlist.copy():
            exist = True
            for letter in letters:
                if letter not in word:
                    exist = False
            
            if not exist:
                wordlist.remove(word)

    for c in not_in:
        for word in wordlist.copy():
            if c in word:
                wordlist.remove(word)
    return wordlist

wordlists = set([file.split('.')[0] for file in listdir(DATA_FOLDER)])
print('allowed wordlists:', wordlists)

wordlist = input('name of wordlist to use? ')
while wordlist not in wordlists:
    wordlist = input('invalid, enter a valid name? ')

with open(f'{DATA_FOLDER}/{wordlist}.txt') as fp:
    words = fp.readlines()

words = [word.strip() for word in words]
print('added', len(words), 'words to analysis')

# TODO: analyze which guess is the most likely to remove the most words
# for now, just pick a random word

while len(words) > 1:
    guess = choice(words)
    print(len(words), 'left, next guess is:', guess)

    word, letters, not_in = return_correctness(guess)
    words = remove_possible(word, letters, not_in, words)

    print(word, letters, words)
