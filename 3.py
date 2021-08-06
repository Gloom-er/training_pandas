import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(6), index=['q', 'w', 'e', 'r', 't', 'y'])
print(s)
print(s + s)
print(s * s)
print(s ** 2)
print(s.astype(np.int16))

pd.read_csv('./MySeries.csv', nrows=1)  # Чтение csv файлов с количеством строк
s.to_csv('./MySeries.csv')

# pd.read_excel('file.xlsx')
# pd.to_excel('dir/MySeries.xlsx', sheet_name='Sheet1')
# df.to_json(filename)
# pd.read_json(json_string)
# pd.read_html(url)
# pd.read_clipboard()


'''
engine = create_engine('sqlite:///:memory:')
pd.read_sql("SELECT * FROM my_table;", engine)
pd.read_sql_table('my_table', engine)
pd.read_sql_query('SELECT * FROM my_table;', engine)
pd.to_sql('MyDf', engine)
'''