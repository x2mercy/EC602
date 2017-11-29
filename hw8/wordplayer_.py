# Copyright 2017 ChenRui ruirui@bu.edu

from sys import argv
from collections import defaultdict
from itertools import combinations

dic = defaultdict(lambda: defaultdict(list))

with open(argv[1]) as file:
    for line in file:
        line = line[:-1]
        dic[len(line)][''.join(sorted(line))].append(line)


while True:
    ans = []
    line = input()
    line = line.split(' ')
    length = int(line[1])
    letter = sorted(line[0])
    if int(line[1]) == 0:
        break
    if len(line[0]) == int(line[1]):
        ans = dic[int(line[1])][''.join(letter)]
    elif (len(line[0]) - int(line[1])) < 5:
        comblist = set(list(combinations(letter,length)))
        comblist = [''.join(comb) for comb in comblist]
        for comb in comblist:
            if comb in dic[length]:
                for i in dic[length][comb]:
                    ans.append(i)
    else:
        word_same_num = dic[length]
        for word in word_same_num:
            input_word = list(line[0])
            temp = []
            for letter in word:
                try:
                    input_word.remove(letter)
                    temp.append(letter)
                except ValueError:
                    break
            if ''.join(temp) == word:
                for item in word_same_num[word]:
                    ans.append(item)
    for item in sorted(ans):
        print(item)
    print('.')
