# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc


def longest_string(s):
    length = 0
    for i in range(0, len(s) - 1):
        j = i
        while s[j] <= s[j + 1]:
            if j == len(s) - 2:
                break
            if length < len(s[i:j + 2]):
                length = len(s[i:j + 2])
                my_string = s[i:j + 2]
            j += 1
    return my_string


print(longest_string('azcbobobegghakl'))
print(longest_string('abcbcd'))
print(longest_string('azcbcd'))
print(longest_string('azcbcdefghe'))