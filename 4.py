import pandas as pd
import numpy as np

data = [[4, 7, 10], [5, 8, 11], [6, 9, 12]]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
print(df)

data = {'Name': ['jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Adress': ['Delphi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Pnd']}

print(pd.DataFrame(data))
pd.DataFrame(data).to_csv('./MyFrame.csv')
df = pd.read_csv('./MyFrame.csv', sep=',', nrows=10)
print(df)
print(df.head(3)) # 3 первые строки
print(df.tail(3))
df.info()
print(df.describe())
print(df.shape)
print(df.ndim)
print(df.size)
print(df.index)
print(df.columns)
print(df.count())
print(df.value_counts())

df = pd.read_csv('./MyFrame.csv', sep=',', nrows=10)
print(df['Age'].value_counts())

df.index = pd.date_range('2020/1/30', periods=df.shape[0])
print(df)

print(df['Name'].nunique())
print(df['Name'].unique())

