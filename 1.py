import pandas as pd
import numpy as np

data = ["Pandas", "Matplotlib", "Numpy"]
s = pd.Series(data)
print(s)
s = pd.Series([2, np.nan, 7, -3, 0])
print(s)
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)
s = pd.Series(np.random.randn(6), index=['q', 'w', 'e', 'r', 't', 'y'])
print(s)
print(s.index)
n = {'q':1, 'w':2, 'e':3}
print(pd.Series(n))
print(s.dtype)
print(s.shape)
print(s.ndim)
print(s.size)
print(s.to_numpy())