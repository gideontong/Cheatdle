from itertools import combinations
from tqdm import tqdm
from json import dump
from math import comb

with open('data/wordle.txt') as fp:
    words = [x.strip() for x in fp.readlines()]

out = list()
with tqdm(total=comb(len(words), 3)) as bar:
    for word in combinations(words, 3):
        if len(set(''.join(list(word)))) == 15:
            print(word)
            out.append(word)
        bar.update(1)

with open('data/triple.json') as fp:
    dump(out, fp)