# Name: Huzaifa Shoeb, ID: 1925670

import csv

file = input()

with open(file, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        words_list = row

        no_duplicates = list(dict.fromkeys(words_list))
        list_length = len(no_duplicates)

        for i in range(list_length):
            print(no_duplicates[i], words_list.count(no_duplicates[i]))
            list[i], words_list.count(no_duplicates[i])

