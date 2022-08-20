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
