# Name: Huzaifa Shoeb, ID: 1925670

import csv

name = input()
with open(name, 'r') as file:
    Reader = csv.reader(file, delimiter=',')
    words = dict()
    for i in Reader:
        for x in i:
            if x in words:
                words[x] = words[x] + 1
            else:
                words[x] = 1
    for n in list(words.keys()):
        print("{} {}".format(n, words[n]))
