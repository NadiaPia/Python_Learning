# def collinearity(x1, y1, x2, y2):
#     if ((x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0)):
#         return(True)
#     elif (y1 == 0 and y2 == 0):
#         return(True)
#     elif (x1 * y2 == x2 * y1):
#         return(True)    
#     else:
#         return(False)

# print(collinearity(5,7,0,0))

#=========Convert a string to an array==============================

# def string_to_array(s):     
#     return(s.split(' '))

# print(string_to_array(''))

#=========Counting sheep...==============================
# def count_sheeps(sheep):
#     return sheep.count(True)

# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))

#=========Is it even?==============================

# def is_even(n): 
#     if (n % 2 == 0):
#         return True

#----better way-----------------------------------------
# def is_even(n): 
#     return n % 2 == 0

# print(is_even(5))

#=========Rock Paper Scissors!==============================
# def rps(p1, p2):
#     if (p1 == p2):
#         return "Draw"
#     round = (p1, p2)
#     game = {
#     ("scissors", "paper"): "Player 1 won!",
#     ('paper', 'scissors'): "Player 2 won!",
#     ("scissors", "rock"): "Player 2 won!",
#     ("rock", "scissors"): "Player 1 won!",
#     ("rock", "paper"): "Player 2 won!",
#     ("paper", "rock"): "Player 1 won!"
#    }

#     return(game[round])


# def rps(p1, p2):
#     beats = {
#         'rock': 'scissors',
#         'scissors': 'paper', 
#         'paper': 'rock'
#     }
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

# print(rps("paper", "scissors"))

# def rps(p1, p2):
#     if (p1 == p2):
#          return "Draw"
#     beats = {
#         'rock': 'scissors',
#         'scissors': 'paper', 
#         'paper': 'rock'
#     }
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"
    

# print(rps("scissors", "paper"))

#=========Removing Elements========================

# def remove_every_other(my_list):
    
#     print(my_list[::2]) # shows only elements in every 3 steps
#     #print(my_list) # save original ["Nadia", "Tania", "Petia", "Sonia", "Fedia", "Luba", "Zina"]

# #remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep"])
# remove_every_other(["Nadia", "Tania", "Petia", "Sonia", "Fedia", "Luba", "Zina"])

#=========Will you make it?========================

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left

# print(zero_fuel(150, 25, 2))


#=========Convert to Binary========================
# def to_binary(n):
#     return int(bin(n)[2::])
# print(to_binary(5))

#=========Will there be enough space?========================

# def enough(cap, on, wait):
#    left = on + wait - cap
#    #return 0 if left < 0 else left
#    return max(0, left)

# print(enough(20, 15, 5))


#=========Square(n) Sum=======================
# def square_sum(numbers):
#     # new_list = []
#     # for el in numbers:
#     #     new_list.append(el**2)

#     # return(sum(new_list))

#     return sum(x**2 for x in numbers)

# print(square_sum([0, 3, 4, 5]))

#=========Find Maximum and Minimum Values of a List=======================

# def minimum(arr):
#     return min(arr)

# def maximum(arr):
#     return max(arr)

# print(maximum([4,6,2,1,9,63,-134,566]))
# print(minimum([4,6,2,1,9,63,-134,566]))

#===========Count of positives / sum of negatives======================

# def count_positives_sum_negatives(arr):
#     result_array = []
#     if arr == []:
#         return []  
#     result_array.append(len([x for x in arr if x > 0]))
#     result_array.append(sum(x for x in arr if x <= 0))

#     return result_array

# print(count_positives_sum_negatives([]))

# def count_positives_sum_negatives(arr):
#     pos = []
#     neg = []
#     for x in arr:
#         if (x > 0):
#             pos.append(x)
#         else:
#             neg.append(x)

#     return [len(pos), sum(neg)] if len(arr) else []

# print(count_positives_sum_negatives([1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]))
# print(count_positives_sum_negatives([]))

#===========Grasshopper - Debug sayHello======================
# def say_hello(name):
#     return "Hello, " + name

# print(say_hello('Mr. Spock'))

#===========Reversed sequence======================
# def reverse_seq(n):
#     #return(list(range(1, n+1)))[::-1]
#     return list(range(n, 0, -1))  #end, start (not including), step

 
# print(reverse_seq(5)) # [5,4,3,2,1]

#===========Sum without highest and lowest number======================
# def sum_array(arr):
#     if arr and len(arr) > 1:
#         new_arr = arr[:] #copy
#         new_arr.remove(max(arr))
#         new_arr.remove(min(arr))

#         return(sum(new_arr))
#     return 0


# def sum_array(arr):
#     if arr and len(arr) > 1:
#          return sum(arr) - max(arr) - min(arr)
#     return 0
        
# print(sum_array([6, 2, 1, 8, 10]))

#===========altERnaTIng cAsE <=> ALTerNAtiNG CaSe======================
# def to_alternating_case(string):
#     arr = []
#     for el in string:
#         if (el.islower()):
#              arr.append(el.upper())
#         else:
#             arr.append(el.lower())
#     return(''.join(arr))

# print(to_alternating_case("hello WORLD"))

#-------------------------------------------------------

# def to_alternating_case(string):
#     return ''.join([c.upper() if c.islower() else c.lower() for c in string]) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#------------the better way----------------------------------

# def to_alternating_case(string):
#     return string.swapcase()

#-------------------------------------------------------
#print(to_alternating_case("hello WORLD"))

#===========Find numbers which are divisible by given number======================
# def divisible_by(numbers, divisor):
#     arr = []
#     for el in numbers:
#         if el % divisor == 0:
#             arr.append(el)
#     return arr

# print(divisible_by([0,1,2,3,4,5,6], 4)) # [2,4,6]

#-------------------------------------------

# def divisible_by(numbers, divisor):
#     return [x for x in numbers if x%divisor == 0] #!!!!!!!!!!!!!!!!!!!!!!!! return [x for x in numbers if x % divisor == 0] !!!!!!!!!!!!!!!

# print(divisible_by([0,1,2,3,4,5,6], 4)) # [2,4,6]

#===========Basic Mathematical Operations======================
# def basic_op(operator, value1, value2):
#     if (operator == '+'):
#         return value1 + value2
#     elif (operator == '-'):
#         return value1 - value2
#     elif (operator == '*'):
#         return value1 * value2
#     elif (operator == '/'):
#         return value1 / value2    

# print(basic_op('+', 4, 7))

#===========Price of Mangoes======================

# def mango(quantity, price):
#     return (quantity - int(quantity / 3)) * price

# print(mango(8, 5))
# print(mango(3, 3))
# print(mango(9, 5))

#===========Printing Array elements with Comma delimiters======================

# def print_array(arr):
#     comma = ","
#     return(comma.join(str(x) for x in arr))


# print(print_array(["hello", "this", "is", "an", "array!"]))
# print(print_array([1, 2, 3, 4, 5]))
# print(print_array([False, True, False, False]))

#===========Welcome===================================================================
# welc = [ 
#     ("english", "Welcome"),
#     ("czech", "Vitejte"),
#     ("danish", "Velkomst"),
#     ("dutch", "Welkom"),
#     ("estonian", "Tere tulemast"),
#     ("finnish", "Tervetuloa"),
#     ("flemish", "Welgekomen"),
#     ("french", "Bienvenue"),
#     ("german", "Willkommen"),
#     ("italian", "Benvenuto"),
#     ("latvian", "Gaidits"),
#     ("lithuanian", "Laukiamas"),
#     ("polish", "Witamy"),
#     ("irish", "Failte"),
#     ("spanish", "Bienvenido"),
#     ("swedish", "Valkommen"),
#     ("welsh", "Croeso"),
# ]

# def greet(language):
#     if (language):
#         for x in welc:
#             if (x[0] == language):
#                 return(x[1])
#     return "Welcome"

    
    #return x[1] for x in welc if (x[0] == language)
    

#print(greet('swedish'))
#return(welc[1][1])
#-------------------------------------------------.get() for dictionaries!!!!!!!!!!!-----------------------
# db = {
#     'english': 'Welcome',
#     'czech': 'Vitejte',
#     'danish': 'Velkomst',
#     'dutch': 'Welkom',
#     'estonian': 'Tere tulemast',
#     'finnish': 'Tervetuloa',
#     'flemish': 'Welgekomen',
#     'french': 'Bienvenue',
#     'german': 'Willkommen',
#     'irish': 'Failte',
#     'italian': 'Benvenuto',
#     'latvian': 'Gaidits',
#     'lithuanian': 'Laukiamas',
#     'polish': 'Witamy',
#     'spanish': 'Bienvenido',
#     'swedish': 'Valkommen',
#     'welsh': 'Croeso',
# }

# def greet(language):    
#     return db.get(language, 'Welcome')
# print(greet('estonian'))

#===========Welcome===================================================================
# def xor(a,b):
#     # if (a != b):
#     #     return True
#     # return False

#     return a != b

# print(xor(False, False))

#===========Reversing Words in a String===================================================================
# def reverse(st):    
#     return " ".join(st.split(" ")[::-1])

# print(reverse('Hello World'))  # 'World Hello'
# print(reverse('Hi There.'))  

#===========validate code with simple regex===================================================================

# def validate_code(code):
#     x = str(code)[0]
#     return x == '1' or x == '2' or x == '3'

# print(validate_code(523)) # True

#-------------------the better way----------------
# def validate_code(code):
#     return str(code)[0] in '123'

# print(validate_code(523)) # True

#-----------------------------------------------------------print('f' in 'funny')

#===========Simple Fun #352: Reagent Formula===================================================================

# material1 and material2 cannot be selected at the same time
# material3 and material4 cannot be selected at the same time
# material5 and material6 must be selected at the same time
# material7 or  material8 must be selected(at least one, or both)

# def is_valid(formula):
    
#     if 1 in formula and 2 in formula:
#         return False     
#     if 3 in formula and 4 in formula:
#         return False    
#     if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
#         return False   
#     if 7 not in formula and 8 not in formula:
#         return False   
#     return True


# print(is_valid([7, 8]))  # Output: True


#===========Remove duplicates from list===================================================================

# def distinct(seq):
#     arr = []
#     for x in seq:
#         if x not in arr:
#             arr.append(x)
#     return(arr)
    
# print(distinct([9, 14, 5, 2, 5, 14]))
#print((distinct([123, 9, 2, 2, 3, 3, 4, 4, 5, 123, 6, 7, 7, 7]))) # [1, 2]

def distinct(seq):
    return sorted(set(seq), key = seq.index)

# Steps:
# set(seq):

# Converts the list seq into a set.
# A set automatically removes duplicates because it cannot contain repeated elements.
# However, the set does not preserve the original order of the elements (since sets are unordered collections).
# sorted(..., key=seq.index):

# After creating the set, the sorted function is used to reorder the elements.
# The key=seq.index argument tells sorted to sort the elements based on their first occurrence in the original list seq.
# seq.index(x) gives the index of the first appearance of x in seq. This means sorted will restore the original order of elements as they appeared in the list.

#===========I love you, a little , a lot, passionately ... not at all===================================================================
# expression = {
#     1: "I love you",
#     2: "a little",
#     3: "a lot",
#     4: "passionately",
#     5: "madly",
#     6: "not at all"
# }

# def how_much_i_love_you(nb_petals):    
#     if(nb_petals <= 6):
#         return expression[nb_petals]
#     elif(nb_petals % 6 == 0):
#         return expression[6]
#     else:
#         return expression[nb_petals % 6]     

# print(how_much_i_love_you(173))

#=========Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string=========================

# def remove(st):
#     arr = []
#     for i,x in enumerate(st):
#         if(x == '!' and i != len(st) - 1):
#             continue       
#         arr.append(x)
#     return("".join(arr))        

# print(remove("Hi! Hi!"))


# def remove(st):
#     arr = []
#     for x in st:
#         if x == '!':
#             continue       
#         arr.append(x)
    
#     return "".join(arr) + "!" 

# print(remove("Hi"))
#---------------------------the better way-----------------------
# def remove(st):
#     return st.replace("!", "") + "!"

# print(remove("Hi"))
# print(remove("Hi! Hi!"))


#=============================================Love vs friendship=============================================
# def words_to_marks(s):
#     db = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 
#     'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
#     'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 
#     'w': 23, 'x': 24, 'y': 25, 'z': 26
#     }  

#     count = 0
#     for x in s:
#         count += (db[x])
#     return count

    

# print(words_to_marks('knowledge')) # 75

#----------------------the better way--------------------------.index()

# def words_to_marks(s):
#     return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)

# print(words_to_marks('knowledge')) # 75

#===================================================================================
#basket = ['a', 'x', 'b', 'c', 'd','e', 'd']
# basket = "_Nadia"


# print(basket.index('i'))

#===================================================V A P O R C O D E======================================================================

def vaporcode(s):
    return "  ".join("".join(s.upper().split(" ")))

print(vaporcode("Lets go to the movies"))