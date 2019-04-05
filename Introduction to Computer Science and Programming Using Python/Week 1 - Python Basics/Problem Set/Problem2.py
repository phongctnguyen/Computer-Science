# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

def number_of_bob(s):
    count = 0
    for num in range(2, len(s) - 1):
        if  s[num-2] + s [num-1] + s[num] == 'bob':
            count += 1
    return f'Number of times bob occurs is: {count}'

print(number_of_bob('azcbobobegghakl'))