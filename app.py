from os import listdir
from collections import Counter

DATA_FOLDER = 'data'

def return_correctness(word: str) -> tuple:
    ans = [None] * 5
    letters = [[], [], [], [], []]
    not_in = set()
    for i, c in enumerate(word):
        prompt = input(f'was {c} correct (yes/misplaced/no)? ')
        if prompt == 'yes':
            ans[i] = c
        elif prompt == 'misplaced':
            letters[i].append(c)
        elif prompt == 'no':
            not_in.add(c)
    
    return ans, letters, not_in

def remove_possible(ans: list, letters: list, not_in: set, wordlist: list) -> list:
    for i, c in enumerate(ans):
        if c:
            for word in wordlist.copy():
                if word[i] != c:
                    wordlist.remove(word)
    
    all_letters = list(set([j for s in letters for j in s]))
    if len(all_letters) > 0:
        for word in wordlist.copy():
            exist = True
            for letter in all_letters:
                if letter not in word:
                    exist = False
            
            if not exist:
                wordlist.remove(word)
    
    for i, letterbox in enumerate(letters):
        for word in wordlist.copy():
            for letter in letterbox: 
                if word[i] == letter:
                    wordlist.remove(word)

    for c in not_in:
        for word in wordlist.copy():
            if c in word:
                wordlist.remove(word)
    return wordlist

def words_with(wordlist: list, characters: list) -> list:
    words = list()
    for word in wordlist:
        included = True
        for c in characters:
            if c not in word:
                included = False
        
        if included:
            words.append(word)
    return words

def choice(wordlist: list) -> str:
    characters = Counter()
    for word in wordlist:
        characters.update(word)
    
    for i in range(6, 1, -1):
        tracking = [i[0] for i in characters.most_common(i)]
        available = words_with(wordlist, tracking)
        if len(available) > 0:
            return available[0]
    
    return wordlist[0]

wordlists = set([file.split('.')[0] for file in listdir(DATA_FOLDER)])
print('allowed wordlists:', wordlists)

wordlist = input('name of wordlist to use? ')
while wordlist not in wordlists:
    wordlist = input('invalid, enter a valid name? ')

double = input('dordle mode (yes/no)? ')
double = double == 'yes'

with open(f'{DATA_FOLDER}/{wordlist}.txt') as fp:
    words = fp.readlines()

words = [word.strip() for word in words]
print('added', len(words), 'words to analysis')

while len(words) > 1:
    guess = choice(words)
    print(len(words), 'left, next guess is:', guess)

    word, letters, not_in = return_correctness(guess)
    words = remove_possible(word, letters, not_in, words)

if len(words) > 0:
    print('the word was', words[0])
else:
    print('the word was not in my dictionary')
