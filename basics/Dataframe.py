"""
tutorial: https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

print('===== Create ======')

data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

frame = DataFrame(data)
print(frame)
print('-------------------')

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print('-------------------')

obj = Series([4, 7, -5, 3, 10], index=['d', 'b', 'a', 'c', 'e'])
obj2 = Series([8, 1, 2, -21], index=['d', 'b', 'a', 'c'])
print(DataFrame({'col1': obj, 'col2': obj2}))
print('-------------------')

frame3 = DataFrame({'year': {'one': 2000, 'two': 2001, 'three': 2002, 'four': 2001, 'five': 2002},
                    'state': {'one': 'Ohio', 'two': 'Ohio', 'three': 'Ohio', 'four': 'Nevada', 'five': 'Nevada'},
                    'pop': {'one': 1.5, 'two': 1.7, 'three': 3.6, 'four': 2.4, 'five': 2.9}})
print(frame3)
print('\n====== Read =======')
print('frame2.values: \n' + str(frame2.values))
print('-------------------')

print('frame2.shape:\n' + str(frame2.shape))  # rows, cols
print('-------------------')

print('frame2.index:\n' + str(frame2.index))
print('-------------------')

print('frame2.columns:\n' + str(frame2.columns))
print('-------------------')

print('frame2[\'state\']\n' + str(frame2['state']))
print('-------------------')

print('frame2.state\n' + str(frame2.state))
print('-------------------')

print('frame2[[\'state\', \'debt\']]\n' + str(frame2[['state', 'debt']]))
print('-------------------')

print('frame2[\'one\':\'one\']\n' + str(frame2['one':'one']))
print('-------------------')

print('frame2[0:4]\n' + str(frame2[0:4]))
print('-------------------')

print('frame2.reindex([\'two\', \'one\'])\n' + str(frame2.reindex(['two', 'one'])))
print('-------------------')

print('frame2.loc[\'one\':\'three\', [\'state\', \'debt\']]\n' + str(frame2.loc['one':'three', ['state', 'debt']]))
print('-------------------')

print('frame2.loc[:, [\'state\', \'debt\']]\n' + str(frame2.loc[:, ['state', 'debt']]))
print('-------------------')

print('frame2.loc[\'one\':\'one\', [\'state\', \'debt\']]\n' + str(frame2.loc['one':'one', ['state', 'debt']]))
print('-------------------')

print('frame2.loc[\'one\', [\'state\', \'debt\']]\n' + str(frame2.loc['one', ['state', 'debt']]))
print('-------------------')

print('frame2\n' + str(frame2))
print('-------------------')

print('frame2.iloc[0:3, [1, 3]]\n' + str(frame2.iloc[0:3, [1, 3]]))
print('-------------------')

print('frame2.iloc[:, [1, 3]]\n' + str(frame2.iloc[:, [1, 3]]))
print('-------------------')

print('frame2.iloc[0:1, [1, 3]]\n' + str(frame2.iloc[0:1, [1, 3]]))
print('-------------------')

print('frame2.iloc[0, [1, 3]]\n' + str(frame2.iloc[0, [1, 3]]))

print('\n====== Set =======')

print('frame2\n' + str(frame2))
print('-------------------')

frame2['debt'] = 16.5
print('frame2\n' + str(frame2))
print('-------------------')

frame2['debt'] = np.arange(5)
print('frame2\n' + str(frame2))
print('-------------------')

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print('frame2\n' + str(frame2))
print('-------------------')

frame2.name = 'data frame'
frame2.columns.name = 'columns'
frame2.index.name = 'index'
print('frame2\n' + str(frame2))
print('-------------------')

frame2.columns = ['a', 'b', 'c', 'd']
print('frame2\n' + str(frame2))
print('-------------------')

frame2.index = [1, 2, 3, 4, 5]
print('frame2\n' + str(frame2))
print('\n===== Delete ======')

frame2.drop([1, 2], inplace=True, axis=0)
print('frame2\n' + str(frame2))
print('-------------------')

frame2.drop(['a', 'b'], axis=1)
print('frame2\n' + str(frame2))
print('-------------------')

frame2.pop('c')
print('frame2\n' + str(frame2))
print('-------------------')

del frame2['a']
print('frame2\n' + str(frame2))

print('\n== Calculation ==')

print('frame3[\'pop\'] > 2:\n' + str(frame3['pop'] > 2))
print('-------------------')

print('frame3[frame3[\'pop\'] > 2]\n' + str(frame3[frame3['pop'] > 2]))
print('-------------------')

print('frame[\'pop\']\n' + str(frame['pop']))
print('-------------------')

# lambda https://www.w3schools.com/python/python_lambda.asp
print('frame[\'pop\'].apply(lambda x: x**3)\n' + str(frame['pop'].apply(lambda x: x**3)))
print('-------------------')
