import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine', 'Kazakhstan'],
    'population': [17.04, 143.5, 9.5, 45.5, 232.12],
    'square': [2724902, 17125191, 207600, 603628, 123050]
}, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])

df['square'].plot.hist()
plt.show()

d = df.groupby(['square'])['population'].agg(np.mean)
d.plot.hist()
plt.show()

