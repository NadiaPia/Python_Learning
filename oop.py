# class PlayerCharacter:
#     #Class Object Attribute
#     membership = True #this is an object which is not dynamic
#     def __init__(self, name, age):                                    #self is refering to the PlayerCharacter class!!!!!!
#         if (PlayerCharacter.membership):  #if (self.membership) the same
#             self.name = name #attributes, they are dinamic
#             self.age = age

#     # def run(self):
#     #     print('run')

#     def shout(self):
#         print(f'my name is {self.name}')

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player2.attack = 50


# # print(player1.name)
# # print(player2.age)
# # print(player2.attack)
# print(player2)


# print(player2.membership) # True
# print(player1.shout())


# #help(player1)


# class PlayerCharacter:
#     #Class Object Attribute
#     membership = True  
#     def __init__(self, name='anonymous', age=0):
#         if (age > 18):  #if (self.membership) the same
#             self.name = name #attributes
#             self.age = age

#     # def run(self):
#     #     print('run')

#     def shout(self):
#         print(f'my name is {self.name}')

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player2.attack = 50


# print(player1.name)
# print(player2.age)
# print(player2.attack)
# print(player2)


# print(player2.membership) # True
# print(player1.shout())


#help(player1)
#------------------------------------the oldest cat-------------------------------
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# cat1 = Cat('Tom', 5)
# cat2 = Cat('Garfild', 4)
# cat3 = Cat('Mars', 9)

# #print(cat1.age)
# arr = [cat1.age, cat2.age, cat3.age]
# def theOldestCat():    
#     return(max(arr))

# #print(theOldestCat())
# print(f'the oldest cat is {theOldestCat()} years old')

# def theOldestCat(*args):   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!the best way!!!!!!!!!!!!!!!!!!!
#     return max(args)

# print(f'the oldest cat is {theOldestCat(cat1.age, cat2.age, cat3.age)} years old')

#------------------------------------the oldest cat-------------------------------



# class PlayerCharacter:
#     #Class Object Attribute
#     membership = True  
#     def __init__(self, name='anonymous', age=0):
#         self.name = name #attributes
#         self.age = age
    

#     def shout(self):
#         print(f'my name is {self.name}')

#     @classmethod   #decorator
#     def adding_things(cls,num1, num2): #cls the same reason as self
#         #return (num1 + num2)
#     # we can use cls to enstantiate the new object:
#         return cls("Teddy", num1 + num2) # another way to instantiate!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    

#     #in static method we don't have an access to the cls, we use it when we don't need class attribute
#     @staticmethod   #decorator
#     def adding_things(num1, num2):
       
#         return num1 + num2
    

# player1 = PlayerCharacter('Cindy', 44)
# player3 = PlayerCharacter.adding_things(2,3)

# print(player1.adding_things(2,3))
# print(PlayerCharacter.adding_things(2,3))
# print(player3.age)
#=================================================================

# class PlayerCharacter:
#     def __init__(self, name, age): 
#         self.name = name #attributes, they are dinamic
#         self.age = age

#     def run(self):
#         return self

# player1 = PlayerCharacter('Nadia', 37)
# print(player1.run())

#============================================Encapsulation====================================
#Binding fuctions with the data

# class PlayerCharacter:
#     def __init__(self, name, age): 
#         self.name = name
#         self.age = age

#     def run(self):
#         return self
    
#     def speak(self):
#         print(f'my name is {self.name}, and I am {self.age} years old')

# player1 = PlayerCharacter('Nadia', 37)
# player1.speak()

#============================================Abstraction====================================
#hidng not nessecary info - f.e we don't need to know how built in functions work under the hood
# class PlayerCharacter:
#     def __init__(self, name, age): 
#         self.name = name
#         self.age = age

#     def run(self):
#         print('run')
    
#     def speak(self):
#         print(f'my name is {self.name}, and I am {self.age} years old')

# player1 = PlayerCharacter('Nadia', 37)
# player1.speak()


#============================================Public and private variables====================================

# class PlayerCharacter:
#     def __init__(self, name, age): 
#         self._name = name  #undescore means it is a private and should not be modefied
#         self._age = age

#     def run(self):
#         print('run')
    
#     def speak(self):
#         print(f'my name is {self._name}, and I am {self._age} years old')

# player1 = PlayerCharacter('Nadia', 37)
# player1.name = '!!!!'  # easy to overwrite the code above
# player1.speak = 'BOOO'

# print(player1.speak)

#   __init__ underscores - Dunder Method - a convention as it should not be modified

#===========================================Inheritance==================================
#alows new objects to take on the properties of existing objects, so you can inherince classes

class User():
    def sign_in(self): #no __init__ as we don't need to asign any variables
        print('logged in')

#Wizards and Archers are users as well, so we need to inherit the sign_in function by passing the User class as an argument

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))   # True
print(isinstance(wizard1, User))     # True
print(isinstance(wizard1, object))   # bcs wizard1 inherits from Wizard, User and higher object base class which Python comes with



#print(wizard1.sign_in()) #Lodded in




