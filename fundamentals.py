#============FIND DUPLICATES===========================

# some_list = ['a','b','c','b','d','m','n','n']

# new_list = []
# duplicate_list = []

# for item in some_list:  
#     if item in new_list:    
#         duplicate_list.append(item)
#     else: 
#         new_list.append(item)
# print(duplicate_list)
# print(some_list)

# for item in some_list:
#     if (some_list.count(item) > 1):
#         if (item not in duplicate_list):
#             duplicate_list.append(item)

# print(duplicate_list)

#============ FUNCTIONS===========================
# def say_hello():
#     print("hello")

# say_hello()

# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# def show_tree():

#     for item in picture:
#         for el in item:         
#             if (el):
#                 print('*', end='')
#             else:
#                 print(' ', end='')

#         print('')      

# show_tree()
# print(show_tree) #<function show_tree at 0x000001F28C32A3E0> shows place in a memory

#============ PARAMETERS vs ARGUMENTS===========================
#parameters - when we define the function

#defalt parameters (if to call a function without the arguments it will use default paramenters)-------------------------
# def say_hello(name='Petia', emoji='😒'):
#     print(f'hello {name}{emoji}')

#arguments - when we call (invoke) the function

#positional arguments (their positin matters)---------------------------------
#say_hello('Nadia', '😊')

#keyword arguments-------------------------------------
# say_hello(name='Tania', emoji='😊')

#say_hello()

#============RETURN===========================

# def sum(num1, num2):
#     return num1 + num2 

# print(sum(4, 5))

#===========TESLA EXERCISE====================

# def checkDriverAge():
#     age = int(input("What is your age?: "))
    
#     if (age < 18):
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif (age > 18):
#         print("Powering On. Enjoy the ride!")
#     elif (age == 18):
#         print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge()

#===========METHODS VS FUNCTIONS====================
#built in functions:-----------------------
# list()
# print()
# max()
# min()
# input()

# def some_function():
#     pass
# def some_function() #to call a function  

# methods----------------------------------- 
# 'heloooo'.capitalize()

#===========DOCSTRINGS====================
# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)

# #test('!!!!!!!!!')
# # test()
# # len()
# #help(test)
# print(test.__doc__)

#===========CLEAN CODE====================

# def is_even(num):
#     return num % 2 == 0       
# print(is_even(51)) 

#===========ARGS AND KWARGS====================
# *args **kwargs

# def super_func(args):
#     return sum(args)
# print(super_func(1,2,3,4,5)) #TypeError: super_func() takes 1 positional argument but 5 were given

# By adding a star we a letting know that there are several args

# def super_func(*args):
#     print(args) # (1, 2, 3, 4, 5) a tuple
#     print(*args) # 1 2 3 4 5
#     return sum(args)
# print(super_func(1,2,3,4,5))

# def super_func(*args, **kwargs):
#     print(kwargs) # {'num1': 5, 'num2': 10} a dictionary  
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
# print(super_func(1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs !!!!!!!!!!!!!!!!!!!!
# def super_func(name, *args, i='hi', **kwargs):
#     print(kwargs) # {'num1': 5, 'num2': 10} a dictionary  
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
# print(super_func('Nadia', 1,2,3,4,5, num1=5, num2=10))

#===========HIGHEST EVEN EXERCISE====================

# def highest_even(li):
   
#     evens = []    
#     for item in li:
#         if (item % 2 == 0):
#             evens.append(item)
#     return max(evens)

# print(highest_even([10,2,3,4,8,11,18]))


# def highest_even(li):
   
#     new_li = []
#     k = 0
#     for item in li:
#         if (item % 2 != 0):
#             continue
#         else:
#             if (item > k):
#                 k = item
#             else:
#                 continue
#     return k

# print(highest_even([10,2,3,4,8,-14]))

#=================================Walrus operator====================
# a new feature
a = 'heloooooooooooooooooo'
# if (len(a) > 10):  # using len(a) one
#     print(f'too long {len(a)} elements') # using len(a) 2

# to avoid a repetition of the expression 'len(a) in line this code we will use a walrus

# if ((n := len(a)) > 10):
#     print(f'too long {n} elements')

# while ((n := len(a)) > 1):
#     print(n)
    
#     a = a[:-1]
# print(a)


#=================================Scope====================
#Scope - what variables do I have access to?
#1 start with local
#2 parent local
#3 Global



#we don't have an access to the total as it is inside the function, not a global variable

# def some_func():
#     total = 100
# print(total)

#===========================Global key word====================

# total = 0
# print(f"this is total{total}")

# def count():
#     total += 1
#     return total

# print(count())  #UnboundLocalError: cannot access local variable 'total' where it is not associated with a value

# in this case use the word global:

# def count():
#     global total # not good practice as this fuction increases the global total!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     total += 1
#     return total


# print(count())
# print(count())
# print(count())

#----------------------------------------------------------------------------------------------------
# def count(total):
    
#     total += 1
#     return total


# print(count(total))
# print(count(total))
# print(count(total))
# # if we want 3 we can do this:
# print(count(count(count(total))))


#==========================nonlocal====================
# def outer():
#     x = 'local'
#     def inner():
#         nonlocal x  # take from parent local
#         x = 'nonlocal'
#         print("inner", x)

#     inner()
#     print("outer:", x)

# outer() 
    

