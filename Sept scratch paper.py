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

#%%

geo = [1, 2, 3, 4, 5]
import pickle

f1 = open('results.pickle', 'wb')

pickle.dump(geo, f1)

f1.close()

# pickle - fascinating!

#%%

whole = [9, 8, 7, 6]
part = whole.index(6)
# result .. part= 3, because the number 6 is in 3rd position

del whole[part]

# now whole is without the element 6, because deleted it

#%%

big_list = [10, 12, 21, 14, 18, 9, 21, 2, 15, 10, 14, 3]

#%%
# remove first instance of item in parenthesis

big_list.remove(18)


#%%

# removes first instance only of thing in list multiple times

big_list.remove(21)

#%%

# remove all instances of something

# list comprehension version

big_list = [z for z in big_list if z != 14]

#%%

# regular version

def remove_all(seq, value):
    pos = 0
    for item in seq:
        if item != value:
            seq[pos] = item
            pos += 1
    del seq[pos:]

#%%

remove_all(big_list, 10)


#%%

big_list.extend([77, 88, 15, 95, 42, 67, 82, 55, 42, 17, 42])
#%%

# another way

big_list = list(filter(lambda x: x!=42, big_list))

#%%

print("before import")
import math

print("before function_a")
def function_a():
    print("Function A")
    
#%%

print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))

#%%

print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")

#%%

help(dict.pop)

#%%

import pandas as pd
import pandas_datareader as  web # don't have this one # pip install needed
import matplotlib.pyplot as pp
import datetime

#%%

someTuple = (1, 2)
someList = [13, 17]

#%%

b = [1, 2]

#%%

print(b[0])

b[0] = 3

#%%

a = (5,7)

print(a[0]) 

a[0]=15

# can't change a tuple! can change a list!!

#%%

print(id(a))

print(id(b))

#%%

a += (20,)

b += [25]

#%%

print(id(a))
print(id(b))

# id for list is the same (contents are changed), id for tuple is different - replaced prior tuple

# this helps my understanding enormously! 

#%%

# tuple can be used as a key in a dictionary, list can't be

possibleDictkeyfromlist = {b: 1}

# error: unhashable type: 'list'

#%%

possibleDictkeyfromtuple = {a: 1}

# it works! Definitely an odd key since didn't follow the guide, but results the same!

#%%

import numpy as np
l = np.arange(9).reshape(3,3)
print(l)
idx = (1,1)
print(l[idx])

# result is 4 - the 2nd item from 2nd row of array
#%%

edx = [1,1]

#%%
print(l[edx])

# result is the 2nd row or array, twice


# these numpy aspects show that numpy works differently with lists vs tuples also

#%%

words = ["this", "is", "a", "sentence"]
#%%

print('-'.join(words))

# updates what is printed, doesn't change list itself

#%%


new = ["today", "is", "Monday"]

print(id(new))

# id answer 1835318484096

#%%

print('**'.join(new))

print(id(new))

# same id.

#%%

x = {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e':9}
y = {'e':10, 'f': 12, 'g': 14, 'h': 16, 'i': 18}

#%%

# z = x | y   is 3.9, I'm on 3.8 still (gotta upgrade one of these days)

z = {**x, **y}

# this results in the key in both taking its value from the 2nd dictionary in the expression

#%%

x['m'] = 15

# to add an additional key/value pair to an existing dictionary.

#%%

y['f'] = 22

# to change the existing value paired with an existing key, to something else

#%%

y.update({'z': 30})

# another way to add a pair to existing dictionary

#%%

q = {'m': 'stone', 'n': 'rock'}

#%%

x.update(q)

# that works too! Contents don't need to conform in characteristics.

#%%
