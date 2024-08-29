"""
Assignment-1:
Count the frequency of letters in a string and output as
key: value
char:count
Write program using dictionary comprehension
"""
string = "hello"
cnt=0
char_count = {char: string.count(char) for char in string}
print(char_count)


"""
Assignment-2:
create dictionary with string of lengths and output as
key: value
word:length
Write program using dictionary comprehension
"""
words = ["hey", "Hello", "Covid"]
dict={i:len(i) for i in words}
print(dict)

"""
Assignment-3:
Count the frequency of each fruit in a list and output as
key: value
fruit:count
Write program using dictionary comprehension
"""
fruits = ["apple", "banana", "apple", "cherry", "banana"]
cnt=0
str_fre= {s: fruits.count(s) for s in fruits}
print(str_fre)