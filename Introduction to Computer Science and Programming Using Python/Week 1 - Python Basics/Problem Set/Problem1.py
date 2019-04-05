# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
# your program should print:
# Number of vowels: 5
def num_vowels(s):
    count = 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for element in s:
        if element in vowel_list :
            count += 1
    return f'Number of vowels: {count}'

print(num_vowels('azcbobobegghakl'))