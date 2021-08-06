import pandas as pd
import numpy as np

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine', 'Kazakhstan'],
    'population': [17.04, 143.5, 9.5, 45.5, 232.12],
    'square': [2724902, 17125191, 207600, 603628, 123050]
}, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])

print(df.sort_values('square', ascending=True).head(10))
#   print(df.groupby(['Sex'])['PassengersID'].count())
print(df.groupby(['square'])['population'].agg(np.mean))
table = df.pivot_table(index=['square'], columns=['country'], values=None, aggfunc='count')
print(table)

print(df.append(df))
print(pd.concat([df, df], axis=1))
print(df.join(df, on='country', how='inner', lsuffix='_left', rsuffix='_right'))
