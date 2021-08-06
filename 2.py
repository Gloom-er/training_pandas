import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(6), index=['q', 'w', 'e', 'r', 't', 'y'])
print(s)
print(s[0])
print(s[1:5])
print(s[s > 0])
print(s[(s > 0) & (s < 1)])
print(s['t'])
print(s[['q', 't']])
print(s[[4, 2]])

print(np.sin(s))
print(np.abs(s))
print(np.tan(s))

s['world'] = 1000
print(s)

print(s.drop(labels=['q', 'world']))
print(s.sum())
print(s.mean())
print(s.max())

