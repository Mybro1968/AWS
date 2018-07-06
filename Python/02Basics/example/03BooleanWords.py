###
#Name : 03BooleanWords.py
#Author : Gary Christie
#Date : 03 Jul 2018
#Purpose : calculate the alphabetical order of two words
###

word1 = input("please input the first word:   ")
word2 = input("please input the second word:   ")

if word1<word2:
    word1first = True
else:
    word1first = False

if word1first:
    print(word1 + " comes before " + word2)
else:
    print(word1 + " comes after " + word2)
