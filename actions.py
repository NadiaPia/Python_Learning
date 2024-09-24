#==============condition====================

is_old = True
is_licenced = True

# if is_old:
#     print('you are old enough to drive!')
# elif is_licenced:           #other condition
#     print('you can drive now')
# else: 
#     print('checheck')


 
# if is_old and is_licenced:
#     print('you are old enough to drive and you have a licence!')
# else: 
#     print('you are not of age')

#==============Truthy and Falsy====================
# password = '123'
# username = 'Johny'

# if password and username:
#     print('You are in')

#==============TURNARY OPERATOR====================
#the same as else is if else if statements
# is_friend = True
# can_message = 'message allowed' if is_friend else "not allowed to message"
# print(can_message)

#==============SHORT CIRCUITING====================
# can be done if we use something like OR
# is_Friend = False
# is_User = True

# #print(is_Friend and is_User)
# if is_Friend or is_User:
#     print('best friends forever')

#==============LOGICAL OPERATORS====================
#print(4 > 5)
# print(4 == 5) #equal
# print(1 < 2 > 3 < 4)
# print(0 != 0)
# print(0 >= 0)
# --------------and, or, not---------------------
#print(not(True)) #not is a function

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print('you are a master magican')
# elif is_magician and not(is_expert):
#     print('at least you are getting there')
# elif not(is_magician):
#     print('you need magic powers')

#print(10 == 10.0) # true - equal check for the equality
#print(10 is 10.0) # false - is check for the location in memory where the value is stored is the same

#print([] is []) # false - when the new list is created is is created in a new location => [] and [] a different lists in different location


#==============FOR LOOPS====================
# for item in [1,2,3,4,5,6]:
#     print(item)


# for item in {1,2,3,4,5}:  #-----------------set
#     print(item)

# for item in (1,2,3,4,5):  #-----------------tuple
#     print(item)
#     print(item)
#     print(item)
# print('hi')

# for item in (1,2,3,4,5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c


#==============ITERABLES====================
#ITERABLE - list[], dictionary{key: value }, tuple(), set{}, string
#iterated -> one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# for item in user:
#     print(item) # name age can_swim - printed only keys



# 3 methods for looping dictionaries!!!!!!!!!-----------------------

# for item in user.items():
#    print(item)  # transformed key-value pairs to tuples('name', 'Golem') ('age', 5006) ('can_swim', False)

# for item in user.values():
#    print(item)  # Golem 5006 False

# for item in user.keys():
#    print(item)  # Golem 5006 False

# for key, value in user.items():    
#     print(key, value)  # name Golem  age 5006  can_swim False

# for item in 50:
#     print(item) #will print an arror as integera are not iterable

#==============TRICKY COUNTER===============================
# my_list = [1,2,3,4,5,6,7,8,9,10]

# count = 0
# for item in my_list:    
#     count = count + item
# print(count)

#==============RANGE===============================
# they are useful in for loops!!!!!!!!!!!!!

#print(range(100)) #prints range(0, 100)

#for number in range(0, 10):
    #print(number)
    #print('email list')

#we don't need a number:
# for _ in range(0, 10, 2):    # 2 is step
#     print(_)

# If we need reverse, use this pattern
# for _ in range(10, 0, -1):    
#    print(_)

# for _ in range(10, 0, -2):    
#    print(list(range(10)))

# for _ in range(2):    
#    print(list(range(10)))


#==============ENUMERATE===============================
# is useful if you need the index counter of the item that you looping through

# for i, char in enumerate('Hello'):
#     print(i, char)

# for i, char in enumerate(list(range(100))):
#     print(i, char)
#     if char == 50:
#         print(f'index of 50 is: {i}')


#==============WHILE LOOPS===============================
# i = 0
# while i < 50:
#     print(i)
#     i += 1
#     #i = i + 1
#     break
# else: #will execute only if there is no break
#     print('done with all the work') 

#==============WHILE LOOPS VS FOR LOOPS===============================

my_list = [1,2,3]

# for item in my_list: # is for simple loops or iterating over iterable objects
#     print(item)

# i = 0
# while i < len(my_list): # for example, when we don't know how many itirations
#     print(my_list[i])
#     i += 1

# while True: # the most popular!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     response = input('say something: ')
#     if (response == 'bye'):
#        break 

#==============BREAK CONTINUE PASS============================

for item in my_list: 
    continue
    print(item) #will never get this line

#==============GUI============================

# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# for item in picture:
#     for el in item:         
#         if (el):
#             print('*', end='')
#         else:
#             print(' ', end='')

#     print('')        


# print('hello', end="")
# print('hello')


