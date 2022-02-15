import pandas as pd

df = pd.read_csv('riders.csv')

# Add a string for each character you know the exact position of.
# Use the position in the list desiginate the position in the word.
# if you know the second letter is "o" use [None, 'o', None, None, None]:
word = [None, None, None, None, None]

# Add a string of EACH character you know are "in" the word somewhere
# ie. ['a','b','c','d','e']:
IN = []

# Add a single string of all the characters you know are "out" of the word
# ie. 'abcde':
OUT = ""

pattern = r'(?='

for x in word:
    if x is None:
        pattern = pattern + '[^{}]'.format(OUT)
    else:
        pattern = pattern + '[{}]'.format(x)

pattern = pattern + ')'

for i in IN:
    pattern = pattern + '(?=.*{}.*)'.format(i)

df.loc[df['word'].str.match(pattern)]
print(df)