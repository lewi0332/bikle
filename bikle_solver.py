import pandas as pd

df = pd.read_csv('riders.csv')

word = [None,None, None, None, None]

IN = ['o', 'a', 'c', 'n']
OUT = "bmser"

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
