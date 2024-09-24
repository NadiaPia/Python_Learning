#print(type(2 + 4))
# print(2 ** 4)
#print(5 // 3)
#print(6 % 2)

#print(round(3.1))
#print(abs(-20))

#print(bin(5))
#print(int('0b101', 2))

#user_iq = 190
#print(user_iq)

#a,b,c = 1,2,3
#print(c)

#number = 5
#number += 2

#print(number)

#username = 'coder'
password = 'secret'
long_string = '''
WOW
0 0
---
+++
'''

#print(long_string)

#print(type(int(str(100))))

# Type Conversing

# Formated string
name = "Johnny"
age = 55
#print(f'hi {name}. You are {age} years old')

selfish = '01234567'
#print(selfish[3])
#[start:stop:stepover]]
#print(selfish[2:])
#print(selfish[::2])
#print(selfish[-1])
#print(selfish[::-2])

# fruits = ['apple', 'banana', 'cherry']

# for fruit in fruits:
# print(fruits[0])


# birth_year = input('What year were you burn?')

# print(2024 - int(birth_year))

# =========================================================
#PASSWORD CHECKER

# username = input('username ')
# password = input('password ')
# masked_password = "*" * len(password)

#print(f'{username}, your password, {masked_password}, is 
#{len(password)} letters long')

# =======LIST (unlake strings, lists are mutable)============

#list slicing
amazon_cart = ['nootbooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'

#new_cart = amazon_cart #if I mutate this, I will change the original list
#new_cart = amazon_cart[:] #if I copy this, I will not change the original list

# new_cart[0] = 'gum'


#print(amazon_cart[0:3]) #from 1 to 3
# print(new_cart)
# print(amazon_cart)

# =======MATRIX============

matrix = [
  [1,5,1],
  [0,1,0],
  [1,0,1]
]

#print(matrix[0][1])


#basket = [1,2,3,4]

#.APPEND================================
# basket.append(100) #.append method changes the list, but does not create a new copy of the list, it modifies the list in the place
#new_list = basket

# print(new_list)
# print(basket)

# .insert()===============================
# basket.insert(1, 100)
# #print(new_list)
# print(basket)

# .extend()===============================
#itirates over the list

# new_list = basket.extend([100, 101])
# #print(new_list) #prints None as it does not create a new copy of the list, it modifies the list in the place
# print(basket)

# .removing()===============================

#.pop removes the last item from the list
#basket.extend([100])
#print(basket)
# basket.pop()
# basket.pop()
# basket.pop(0) #removes the item with the index 0 => we give it the index

#.remove removes the last item from the list

# basket.remove(4) #removes the item with the value of 4.
# print(basket)

# .clear 
# new_list = basket.clear()
# print(new_list) #none as it does not create a copy of the list
# print(basket) #[]
#=====================================================

#basket.index(index, start, stop) #shows the index of the item

basket = ['a', 'x', 'b', 'c', 'd','e', 'd']

# print(basket.index('d', 0, 4))
# print('d' in basket)
# print('i' in 'hi my name is Nadia')

# print(basket.count('d'))

#basket.sort() #method modifies the basket and print(basket) shows sorted basket

#print(basket)

#print(sorted(basket)) #function does not modifies array and print(basket) will show the initial array
#print(basket)

# basket.reverse() #reverses in a place
# print(basket)



# new_list = basket.copy()
# print(new_list)

#print(basket.copy())
#print(basket[:])

basket.sort()
basket.reverse()
# print(basket[::-1])
# print(basket)

#=================RANGE=========================
#print(list(range(1,100))) #(start, finish) - will start from 1-100
#print(list(range(100))) #(start, finish) - will start from 0-99

#=================JOIN=========================
sentance = "!"
sentance.join(['hi', 'my', 'name', 'John']) #join() does not mutate => it is a new list => print(sentance) will show initial sentance
new_sentance = sentance.join(['hi', 'my', 'name', 'John'])

#print(new_sentance)
#print(sentance)

#print(' '.join(['do','re','mi','fa'])) #shorter way

#========LIST ANPUCKING=============

#a,b,c = [1,2,3]
#a,b,c = 1,2,3
#a,b,c,*other = [1,2,3,4,5,6,7,8,9]
# a,b,c,*other, d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

#========NONE=============
# weapons = None
# print(weapons)

#========DICTIONARY=============
#it is a data structure

# dictionary = {
#   'a': 1,
#   'b': 2,
#   'x': 3
# }

#print(dictionary['b'])
#print(dictionary)

my_list = [
  {
  'a': [1,2,3],
  'b': 2,
  'x': True
},
{
  'a': [4,5,6],
  'b': 2,
  'x': 3
}
]
#print(my_list[0]['a'][2])

#keys of the dictionary must not be mutated (ex, key can not be a list as list is mutable)

# dictionary = {
#   123: [1,2,3],
#   True: 'hello',
#   # [100]: True       #list can not be a key of a dictionary!!!!!!!!!!!!
# }

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }

#print(user.get('age', 55)) #if 'age' does not exist, get 55, otherwise get value of the 'age'

#another way to create a dictionary:
#user2 = dict(key=value)
#user2 = dict(name = 'JohnJohn') #{'name': 'JohnJohn'}
#print(user2)

#print('i' in ['a', 'i']) #True
#print('i' in 'Nadia') #True
#print('basket' in user) #True
# print('age' in user.keys()) #True
# print('hello' in user.values()) #True
# print(user.items()) #True

#user.clear() #mutates - ghages thr origin dictionary
#user2 = user.copy()
#user2.clear()

# print(user.clear())
# print(user2)

#print(user.pop('age')) #removes and returns what was removed: 20
#print(user.popitem()) #removes the last key:value pair

# print(user.update({'age': 55}))
# print(user.update({'ages': 55})) #will idate with the new key:value 

# print(user)

#===========================Tuples=====================
#it is like an unmutable list

#my_tuple = (1,2,3,4,5) -------------- unmutable list
#my_tuple = [1,2,3,4,5] -------------- mutable list

#the example of a mutable list
# my_tuple = [1,2,3,4,5]
# my_tuple[2] = 100
# print(my_tuple[2])
# print(my_tuple)
# print(type(my_tuple)) #list

#my_tuple = (1,2,3,4,5)


#my_tuple[2] = 100 #we cannot change tuple like that
#print(my_tuple[2])
#print(5 in my_tuple)
 
# user = {
#   "basket": [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }
#print(user.items()) #([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)]) looks like list of tuples

# user = {
#   (1, 2): [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }

# print(user[(1,2)])

#new_tuple = my_tuple[1:2]
#x,y,z, *other = (1,2,3,4,5)
#print(new_tuple) #(2,)
# print(z)
# print(other)

# my_tuple = (1,2,3,4,5,5)


# print(my_tuple.count(5)) #count how many 5 
# print(my_tuple.index(5)) #count how many 5 
# print(len(my_tuple))

#=================SET======================
#unordered collection of unique objects

my_set = {1,2,3,4,5, 5} # will return only unique sets (no any duplicates):{1, 2, 3, 4, 5}

#my_set.add(100) # {1, 2, 3, 4, 5, 100}
#my_set.add(2) # {1, 2, 3, 4, 5, 100}

#print(my_set)
#print(type(my_set))

#my_list2 = [1,2,3,4,5,5,200]
#print(my_list2)
#print(set(my_list2))

#print(my_set[1]) # doesn't work
# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))

# my_set2 = my_set.copy()
# my_set2.clear()


# print(my_set2)
# print(my_set)

nadia_set = {1,2,3,4,5}
tania_set = {4,5,6,7,8,9,10}
katia_set = {4,5}
#----------------------------.difference---------------------------

#print(nadia_set.difference(tania_set)) #{1,2,3} ignores duplicates and shows only difference

#print(tania_set.difference(nadia_set)) #{6, 7, 8, 9, 10}

#----------------------------.discard ----------------------------
# (removes an element if it is a member)

#print(nadia_set.discard(5)) #None => modifies the origin set
#print(nadia_set) #{1, 2, 3, 4} - discarded 5

#----------------------------.difference_update-------------------------
#(removes all elements of another set from this set)

#print(nadia_set.difference_update(tania_set))
#print(nadia_set) # print(nadia_set) modifies the origin set

#----------------------------.intersection ----------------------------
#print(nadia_set.intersection(tania_set)) #{4,5}
#print(nadia_set & tania_set) # a shortcut!!!!!!!!!!!!


#----------------------------.isdisjoint ----------------------------
#print(nadia_set.isdisjoint(tania_set)) #false because they have something common

#----------------------------.union ----------------------------
#print(nadia_set.union(tania_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} unites sets, but removes all duplicates

#print(nadia_set | tania_set) # a shortcut!!!!!!!!!!!!

#----------------------------.issubset ----------------------------

#print(katia_set.issubset(tania_set)) #true - as katia is inside the circle of the ania_set 

#----------------------------.issuperset ----------------------------
#print(tania_set.issuperset(katia_set)) #true





 






























