import numpy as np
import pandas as pd

my_index = ['a', 'b', 'c']
my_values = [222, 333, 444]
my_dict = {'a': 222,
           'b': 333,
           'c': 444}

my_arr = np.array(my_dict)
print(my_arr)

print('-----------Series with values.------------------')
print(pd.Series(my_values))

print('------Series with values and index labels.------')
print(pd.Series(data=my_values, index=my_index))

print('-------Series from a NumPy array.---------------')
print(pd.Series(my_arr))

print('--Series from a NumPy array with index labels.--')
print(pd.Series(my_arr, index=my_index))

print('----------Series from a dictionary.-------------')
print(pd.Series(my_dict))

print('------------------------------------------------')
s = pd.Series(data=[111, 222, 333, 444], index=['a','b','c','d'], name='MySeries')
print(s)

print('----------Index labels.------------')
print(s.index)            
print('----------Name attribute.------------')                       
print(s.name)              
print('----------Data type.------------')                      
print(s.dtype)     
print('----------The values as NumPy array.------------')                              
print(s.values)

print('------------------------------------------------')
print(s.iloc[1])
print(s.loc['a'])
print(s.iloc[2:4])
print(s.loc[['a','d']])

print('------------------------------------------------')
s1 = pd.Series(data=[1, 2, 3, 4], index=['d', 'b', 'c', 'a'])
s2 = pd.Series(data=[1, 2, 3, 4], index=['a', 'b', 'd', 'e'])

print(s1 + s2)

print('-------------Ham tinh toan----------------------')
print(s1.sum())
print(s1.mean())
print(s1.median())
print(s1.max())
print(s1.std())
print('------------------------------------------------')
print(s1.sort_values())
print(s1.sort_index())

print('------------------------------------------------')

ser_height = pd.Series([165.3, 170.1, 175.0, 182.1, 168.0, 162.0, 155.2, 176.9, 178.5, 176.1,
                        167.1, 180.0, 162.2, 176.1, 158.2, 168.6, 169.2], name='height')
ser_height