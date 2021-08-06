import pandas as pd
import numpy as np

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine', 'Kazakhstan'],
    'population': [17.04, 143.5, 9.5, 45.5, 232.12],
    'square': [2724902, 17125191, 207600, 603628, np.nan]
}, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])

print(df)
print(df.isna()[0:])   # Проверка пустых значений
df2 = df.dropna()   # Для удаления столбцов с null values
df = df.fillna((df['square'].mean()))   # Значение подставяется во все пустые строки
print(df)

