"""
Assignment-1:
WAP to find names starts with ‘A’ and ends with 'a'
in the given list of names using list comprehension
"""
names = ['Abeesha', 'Abelia', 'Anil', 'Shanvika', 'Jayansh']
filtered_names = [name for name in names if name.startswith('A') and name.endswith('a')]
print(filtered_names)


"""
Assignment-2:
WAP to extract each word from a sentence and store all the words
in the form of list using list comprehension
"""

paragraph = ["There was a fox.", 'It was brown in color.', "It was seen near that farm sometime back"]
filtered_paragraph=[w for i in paragraph for word in i.split(".") for w in word.split() ]
print(filtered_paragraph)