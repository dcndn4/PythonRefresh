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
z = {**x, **y}

#%%