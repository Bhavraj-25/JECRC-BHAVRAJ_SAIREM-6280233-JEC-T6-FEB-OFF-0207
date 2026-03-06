# In-Built functions

# utility fnc: can be used on all data types (eg. dir, help)

## Functions for string data types:
'''
    lower, upper, capitalize, title, strip, lstrip, rstrip, replace, index, split, join, startswith, endswith, isdigit, isalpha, islower, isupper
'''

s = 'pyThOn'
print(s.lower())
print(s.upper())
print('pYTHON is great'.capitalize())
print('python is a great language'.title())
print('/// python used everywhere'.lstrip('/// '))
print('python used in robotics ///'.rstrip(' ///'))
print('python / is / great'.split('/'))
print('python pis pgreat'.strip('p'))
print('python woohahaha'.replace('woohahaha', 'hihaha'))

S = 'python can be used for CVision be'
T = 'i love biriyani very much'
U = 'python is great'
print(S.find('az')) # if not found returns -1
# print(S.index('az')) # returns value error
res = T.split(' ') # won't return or keep the separator value provided (biriyani won't be printed)
print(res)
print("-".join(res))

print(S.startswith('python'))
print('PYTHON IS HMM'.isupper()) # check if it is upper
print('python is lower'.islower()) # checks if it is lower
print('python1'.isalpha()) # checks if it is alphabetic

## Functions for list data type:
'''
    append, insert, extend, pop, remove, clear, sort, reverse, index, count
'''

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,1,2]
list1.append(69)
list1.insert(0,'a')
print(id(list1))
list1.extend(list2)
print(id(list1))
list1.pop()
list1.pop(3)
list1.remove('a')

print(list1, list2)
# list2.clear()
# print(list2)
list1.sort() # for descending put reverse=True as argument i.e. sort(reverse = True)
print(list1)
print(list1.index(69))
print(list1.count(1))
list2.reverse()
print(list2)

# ## Functions for Tuple data type:
'''
     index, count
'''

tup1 = (1,2,3,4,5)
tup1.index(1)
tup1.count(5)

## Functions for set data type: ((set doesn't store values consecutively, instead in random way), only allows immutable types
'''
    add, remove, pop, discard, clear
'''

set1 = {1, 2, 0.5, 6, True, (10, 20)}

set1.add(1010) # cannnot add list or dict (mutable types)
print(set1)

set1.remove(True) # value should be a member of the set; else throws error
print(set1)

set1.discard(False) # does not raise exception when an element is not present in set
set1.discard(2)
print(set1)

set1.pop() # randomly pops out value; takes no argument
print(set1)

set1.clear()
print(set1) # empties the set

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.union(s2)) # returns a new set
print(s1.intersection(s2)) # returns intersected element; new set
print(s1.difference(s2)) # returns uncommon element; new set
print(s1.symmetric_difference(s2)) # returns uncommon elements from both sets; new set


## Functions for dictionary data type:
'''
    get, pop, popitem, clear, update, keys, values, items
'''

d1 = {1:'a', 2:'bc', 3:'def', (1, 2, 3):[10, 20, 30]} # keys can only have immutable items
d1.get((1,2,3)) # returns value for the mentioned key
d1.get('5') # unidentified keys throw none; not error
d1.pop(1) # remove using specified key; gives value associated with the key in return
print(d1)

user = {
    'uname': 'XYZ',
    'password': '********',
    'location': 'IN',
    'mail': 'xyz@gmail.com'
}

print(user.popitem()) # removes and returns key-value pair in tuple; returns keyError if item is not present
print(user)

user.update({'password':123}) # overwrites the existing value
user.update({'number':9090906969}) # adds new item if it is not present
print(user)


## PACKING

def add_fnc(*args):
    args = list(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)


# add_fnc(1, 2, 3, 4, 5) # single packing type

def x_fnc(*args):
    sum = 0
    for i in args:
        if type(i) in [int, float, complex]:
            sum += i
    print(sum)

x_fnc(1, 2, True, None, 1+0j, 0.25) # single packing type


# DOUBLE PACKING
# All the key names should be a string but can't use quotes; f_name(key='val', key2='val'); returns in dictionary
def print_det(**kwargs):
    print(kwargs)

print_det(username = 'xyz', password = '*******', location = 'IN', logged_in = ['win', 'linux'])

add_fnc(*eval(input("enter input values: "))) # takes list and unpacks the values

## Prime/not prime

def print_nt(*args):
    prime = []
    for i in args:
        if type(i) in [int]:
            if(isPrime(i)):
                prime.append(i)
    return prime

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

res = print_nt(*eval(input('enter input: ')))
print(res)