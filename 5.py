import pandas as pd
import numpy as np

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine', 'Kazakhstan'],
    'population': [17.04, 143.5, 9.5, 45.5, 232.12],
    'square': [2724902, 17125191, 207600, 603628, 35445]
}, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])
print(df)
print(df["country"].nunique(), ' ', df['country'].unique())
print(df["country"].value_counts())
print(df["country"].apply(lambda x: x.upper()))
print(df.country)   # df["country"]
print(df[['country', 'square']])
print(df.loc['KZ'])
print(df.loc[['KZ'], ['square']])
print(df.iloc[1])
print(df.iloc[1, 1])
print(df.iloc[1, 1:3])
print(df.iloc[1:3, 1:3])
print(df.loc[['KZ', 'RU'], 'square'])
print(df.loc['RU':'UA', :])
print(df[df.population > 30])
print(df[df.population > 30][['country', 'square']])
df['Density'] = df['population'] / df['square'] * 1000000
print(df)
print(df.sum(), '\n\n', df.mean(), '\n\n', df.max())
print(df['square'].mean())
print(df.drop(['square'], axis=1))
