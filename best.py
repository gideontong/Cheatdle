from itertools import combinations
from tqdm import tqdm
from json import dump
from math import comb
from time import sleep

with open('data/wordle.txt') as fp:
    words = [x.strip() for x in fp.readlines()]

with open('best.txt', 'w') as fp:
    with tqdm(total=comb(len(words), 3)) as bar:
        for i, w1 in enumerate(words):
            if len(set(w1)) < 5:
                bar.update((len(words) - i) ** 2)
                continue
            for j, w2 in enumerate(words[i+1:]):
                if len(set(w2)) < 5 or len(set(w1 + w2)) < 10:
                    bar.update(len(words) - j)
                    continue
                for k, w3 in enumerate(words[j+1:]):
                    if len(set(w3)) < 5 or len(set(w1 + w2 + w3)) < 15:
                        bar.update(1)
                        continue
                    nex = f'{w1} {w2} {w3}\n'
                    if all([x in nex for x in 'aeiounptsh']):

                        print(w1, w2, w3)
                    
                    fp.write(nex)
                    bar.update(1)
