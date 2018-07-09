vowel_list=["a","e","i","o","u"]

count_vowel = 0

word = str(input("please input a word:   "))

for char in word:    
    if char in vowel_list:
       count_vowel = count_vowel + 1

print("the number of vowels in ", word, "is ", count_vowel)
