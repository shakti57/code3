#!/usr/bin/env python
# coding: utf-8

# In[1]:
#day32

import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Drop a column
column_to_drop = 'B'
df = df.drop(column_to_drop, axis=1)

print("\nDataFrame after dropping column '{}'".format(column_to_drop))
print(df)

# Drop a row
row_to_drop = 2
df = df.drop(row_to_drop)

print("\nDataFrame after dropping row '{}'".format(row_to_drop))
print(df)


# In[ ]:




