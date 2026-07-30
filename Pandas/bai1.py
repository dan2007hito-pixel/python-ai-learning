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