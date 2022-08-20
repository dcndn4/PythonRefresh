# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 05:03:46 2022

@author: CS_Knit_tinK_SC
"""

# reviewing

import pandas as pd

df = pd.DataFrame({"Car": ['Car 1', 'Car 2', 'Car 3', 'Car 4', 'Car 5'], 
                   "Model": ['Nissan', 'Nissan', 'Toyota', 'Ford', 'Checkers'],
                   "Status": ['Purchased', 'Sold', 'Borrowed', 'Blue', 'Rented']})

print(df)

#%%

df['Occur'] = df[df['Status'] == 'Sold'].groupby('Car')['Model'].transform('size')

#%%

filtered_df=df.loc[df['Occur'] ==1][['Car', 'Model', 'Status']]

print(filtered_df)

#%%

# merge two dictionaries 'shallowly', with vales from y replacing any values from x for same value

x = {'a': 1, 'b':2}
y = {'b': 3, 'c': 4}

#%%
z = {**x, **y}

# this z = syntax was proposed in PEP 448 and in Python 3.5, per S.O. (sigh)
# is in 'what's new in Python 3.5 document
#%%

z = {**x, 'foo': 1, 'br': 2, **y}
print(z)

#%%

from timeit import repeat
from itertools import chain

x = dict.fromkeys('abcdefg')
y = dict.fromkeys('efghijk')

#%%

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

#%%

print(min(repeat(lambda: {**x, **y})))
#%%
print(min(repeat(lambda: merge_two_dicts(x, y))))
#%%

print(min(repeat(lambda: {k: v for d in (x, y) for k, v in d.items()})))

#%%

print(min(repeat(lambda: dict(chain(x.items(), y.items())))))
#%%

print(min(repeat(lambda: dict(item for d in (x, y) for item in d.items()))))

#%%

xs = [8, 23, 45]
#%%
# question
#for x in xs: 
#    print("item #{} = {}".format(index,x))

for idx, x in enumerate(xs):
    print(idx, x)
    
#%%

# to have the first index set to 1:

for idx, x in enumerate(xs, start=1):
    print(idx, x)
#%%

# non-idiomatic option 1

items = [18, 22, 25, 17, 29]

index = 0
for item in items:
    print(index, item)
    index += 1
    
    
#%%

# non-idiomatic option 2

smeti = [37, 82, 1001199, 5, 725, 87]

index = 0
while index < len(smeti):
    print(index, smeti[index])
    index += 1

#%%


# non-idiomatic option 3

hello = [22, 44, 88, 1252, 99999]

for index in range(len(hello)):
    print(index, hello[index])
    
#%%

# to get a count

count = 0 
for count, item in enumerate(hello, start=1):
    print(item)
    
print('there were {0} items printed'.format(count))

#%%

    