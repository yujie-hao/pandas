import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series
s = pd.Series
print(s)
print("=== Create ====")

obj = Series([4, 7, -5, 3], dtype=np.int32)
print(obj)
print("---------------")

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print("---------------")

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)
print("---------------")

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)

print("\n==== Read ====\n")

print("obj[1]: " + str(obj[1]))
print("obj[2]: " + str(obj[2]))
print("---------------")

print("obj2[['c', 'a', 'd']]: \n" + str(obj2[['c', 'a', 'd']]))
print("---------------")

print("obj2: \n" + str(obj2))
print("---------------")

print("obj2[1:3] \n" + str(obj2[1:3]))  # [) --> inclusive, exclusive
print("---------------")

print("obj.index: \n" + str(obj.index))
print("---------------")

print("obj2.index: \n" + str(obj2.index))
print("---------------")

print('obj2.values: \n' + str(obj2.values))

print("\n==== Update ====\n")

obj2['d'] = 6
print('obj2: \n' + str(obj2))

obj2[['a', 'b', 'c']] = [1, 2, 3]
print('obj2: \n' + str(obj2))
print("---------------")

obj4.name = 'population'
obj4.index.name = 'state'
print('obj4: \n' + str(obj4))
print("---------------")

print('obj: \n' + str(obj))
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print('obj: \n' + str(obj))

print("\n==== Delete ====\n")
del obj2['a']
# drop doesn't delete, but return the series without the dropped item
print('obj2.drop(\'c\'): \n' + str(obj2.drop('c')))
print('obj2: \n' + str(obj2))
print("---------------")

print('obj2.drop([\'b\', \'d\']):\n' + str(obj2.drop(['b', 'd'])))
print('obj2: \n' + str(obj2))

print("\n==== Calculate ====\n")

print('b in obj2: ' + str('b' in obj2))

print('e in obj2: ' + str('e' in obj2))

print('obj2: \n' + str(obj2))
print("---------------")

print('obj2 > 4:\n' + str(obj2 > 4))
print('obj2[obj2 > 4]\n' + str(obj2[obj2 > 4]))
print("---------------")

print('obj2 * 2: \n' + str(obj2 * 2))
print("---------------")

print('np.exp(obj2): \n' + str(np.exp(obj2)))  # e = 2.718281828, Euler's number, e^2 = 2.71 ^ 2.71 = 7.3
print("---------------")

print('obj4: \n' + str(obj4))
print('pd.isnull(obj4): \n' + str(pd.isnull(obj4)))
print('\npd.notnull(obj4): \n' + str(pd.notnull(obj4)))
print('\nobj4.isnull: \n' + str(obj4.isnull()))
print('\nobj4.notnull: \n' + str(obj4.notnull()))
print("---------------")

print('obj3: \n' + str(obj3))
print('\nobj4: \n' + str(obj4))
print('\nobj3 + obj4: \n' + str(obj3 + obj4))
print("===============")

