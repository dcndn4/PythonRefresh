# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 05:03:46 2022

@author: CS_Knit_tinK_SC
"""

# reviewing

import pandas as pd
import numpy as np
import datetime
import time
import pytz

#%%

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

#%%

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

# 8.21.22

List1 = ["2,6,4,5", "3,7,4,2"]
#%%
List2 = ["15,2000,65,1", "529, 6123, 777, 82"]

sortedList = []
#%%
# this solution doesn't work for  numbers > 10, not sure why yet

for s in List2:
    nums = s.split(",")
    nums.sort()
    sortedList.append(",".join(nums))
    
#%%

for s in List2:
    nums = s.split(",")
    nums = list(map(int,nums))
    nums.sort()
    nums = list(map(str,nums))
    sortedList.append(",".join(nums))
    
#%%

# using ast.literal eval -- result is printed, but actual list isn't changed

import ast

List3 = ["17,3000,45,3", "659,723,1456,19"]
print([",".join(map(str, sorted(ast.literal_eval(item)))) for item in List3])

#%%

List4 = ["57,259,83,1745", "22222,598,75,3"]

#%%

# this doesn't seem to yield desired result at all.. not sorted, and split by periods.. hmmm..

Output = ['.'.join(sorted(lis)) for lis in [s.split(',') for s in List4]]

#%%

print(np.unravel_index([22, 41, 37], (7,6)))

#%%

x = np.array([[4,  2],
              [9,  3],
              [8,  5],
              [3,  3],
              [5,  6]])

#%%

print(x.shape)

#%%

idx = np.where(x==3)
print(idx)
#%%

idx_flat = np.ravel_multi_index(idx, x.shape)
print(idx_flat)

#%%

x_linear = x.ravel()
print(x_linear)

#%%

idx_new = np.unravel_index(idx_flat , x.shape)
print(idx_new)
#%%

# this response uses a set of random numbers as the starting point, forgot it was that easy to get those

my_array = np.random.random((100, 42))  # 2D set
raveled_array = my_array.ravel()    # 1D set

raveled_index = 1337

#%%

# this is extra confusing to me

unraveled_index = np.unravel_index(raveled_index, my_array.shape)

#%%

assert raveled_array[raveled_index] == my_array[unraveled_index]

#%%

now = datetime.datetime.now()

print(now)

#%%

now.time()

datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
print(now)

#%%



from datetime import datetime

print(datetime.now().strftime('%Y-%m-%d %H:%m:%S'))

#%%

from datetime import localtime, strftime

print(strftime("%Y-%m_%d %H:%M:%S", localtime()))

# Message - cannot import 'localtime' -- hmmm

#%%


print(time.time())

# number of seconds since 1.1.70 0000

#%%

# my fav so far

print(time.ctime())

#%%

print(datetime.datetime.utcnow())

# so UTC is 5 hours ahead of me (at the moment)

#%%

# time zone aware == more on that another time

then = datetime.datetime.now(pytz.utc)

print(then)

#%%

from time import ctime

print(ctime())

# Like!

#%%

# How to sort dictionary

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# dictionary with unsorted contents

#%%
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})

# dictionary contents still unsorted, but printed representation of dictionary is in sorted order
#%%

print(dict(sorted(x.items(), key=lambda item: item[1])))

# same result

#%%

x = [1, 2, 3]

#%%

# officially: this appends object, increases amount of things in list by 1
# this appends a list containing the two integers 4 & 5
x.append ([4, 5])

# running that again appends a second identical (of course)  list

# this appends a new items similar to the original ones, an integer.
x.append(6)

#%%

# officially: this extends list by adding elements - increases amount of things in list by number of elements being added
# extends (with same format as first append), adds the integers themselves
x.extend([7, 8])

#%%

x.extend([101, 500])

# items being added don't need to be next in order obvs..

#%%

z = x + [15, 17]

#%%

new_list = x + [72]

fruit_list = ['apple', 'orange']

new_list.append(fruit_list)

veg_list = ['beet', 'onion']
#%%

new_list.extend(veg_list)
#%%
other_list = [12, 15, 17]

# each element of iterable gets added to list individually

other_list.extend('eighteen')

#%%

Saturday_list = ['chore', 'rest', 'progress']

#%%
# adding the two lists creates a valid result that exists in memory, doesn't have a name etc.. so can't be referenced

print(veg_list + Saturday_list)

#%%

# performance review

def append(alist, iterable):
    for item in iterable:
        alist.append(item)
        
def extend(alist, iterable):
    alist.extend(iterable)
    
#%%

import timeit

print(min(timeit.repeat(lambda: append([], "abcdefghijklmnopqrstuvwxyz:"))))

# result 1.64223

#%%

print(min(timeit.repeat(lambda: extend([], "abcdefghijklmnopqrstuvwxyz:"))))

# result .3787   --- much faster!

#%%

# append, insert and extend!

xs =  ['A', 'B']

xs.append('D')

#%%

xs.append(['E', 'F'])

# upper limit of what you can achieve in one 'append' step is one change -- an item or list (or dictionary?).. to add more 
# than one item at a time, use extend.

#%%

xs.insert(2, 'C')

# puts it in to specific position!

#%%

xs.extend(['G', 'H'])

# formatted same as append above , result is diff: iterated over new items vs. added as a whole (in 'nested' fashion)
# extend is 'implemented in C' .. within .. python..... so there's that. 

#%%

dict1 = {"key1": "booka", "key2": "recordb"}

#%%

import copy

dict2 = copy.deepcopy(dict1)

dict2["key3"] = "soundc"

# deepcopy makes whole different dictionary, separate from original dictionary. Changes to that new, independent dictionary 
# do not affect original dictionary.

# notice of comment - deep copy can introduce 'silent bugs' and should be avoided.. hmmm. related to cyclic
# reference handling possibly, self-referential ordered dictionary. 

# Python objec model - crucial

# seems maybe problems existed in prior versions, now more ok..

# much discussion q 2465921

#%%

forward_list = [0, 10, 20, 30]

print(list(reversed(forward_list)))

#reverse this way does the task of presenting a list contents in reverse order

for x in reversed(forward_list):
    print (x)
    
    
#%%

# other method - slice functionality

print(forward_list[::-1])

#%%

xs.reverse()

#%%

forward_list.reverse()

# doing that does reverse the  list itself. 

# plus more yet!



