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












