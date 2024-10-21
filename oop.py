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

# class User():
#     def sign_in(self): #no __init__ as we don't need to asign any variables
#         print('logged in')

#Wizards and Archers are users as well, so we need to inherit the sign_in function by passing the User class as an argument

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')

# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')

# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 100)
# wizard1.attack()
# wizard1.sign_in()
# archer1.attack()

# print(isinstance(wizard1, Wizard))   # True
# print(isinstance(wizard1, User))     # True
# print(isinstance(wizard1, object))   # bcs wizard1 inherits from Wizard, User and higher object base class which Python comes with



#print(wizard1.sign_in()) #Lodded in


#==========================================================Polymorphism============================
#poly - many
#morphism - forms
#the same methods (attack(may give differen outputs))

# class User():
#     def sign_in(self): 
#         print('logged in')

#     def attack(self):
#         print('do nothing')

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.power}')

# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')

# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 30)

# def player_attack(char):
#     char.attack()

# # player_attack(wizard1)
# # player_attack(archer1)

# # for char in [wizard1, archer1]:
# #     char.attack()
# print(wizard1.attack())

#==========================================Pets everywhere=============================
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def walk(self):
#         return f'{self.name} is just walking around'
    
# class Simon(Cat):
#     def sing(self, sound):
#         return f'{sound}'
    
# class Sally(Cat):
#     def sing(self, sound):
#         return f'{sound}'
    
# #1 Add another Cat
    
# class Jery(Cat):
#     def sing(self, sound):
#         return f'{sound}'
    
# #2 Create a list of all of the pets (create 3 cat instances from the above)

# # my_cats = []
# # cat1 = Simon('Simon', 10)
# # cat2 = Sally('Sally', 5)
# # cat3 = Jery('Jery', 8)

# # my_cats.append(cat1)
# # my_cats.append(cat2)
# # my_cats.append(cat3)
# # OR
# my_cats = [Simon('Simon', 10), Sally('Sally', 15), Jery('Jery', 5)]

# #3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)

# #4 Output all of the cats walking using the my_pets instance

# my_pets.walk()

#======================================super()============================
# class User():
#     def __init__(self, email): #in order to be able to receive an argument from child classes
#         self.email = email

#     def sign_in(self): 
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email): #email is the property of the User class, that is why wec handle it other way then name and power
#         # to have an access to the email in the parent User class!!!
#         #one way:
#         #User.__init__(self, email) 
#         #another way:
#         super().__init__(email) #with the new addition of super we no longer need a "self"

#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')

# print(wizard1.email)

#=====================================introspection============================
#is the ability to determin the type of an object at runtime
# class User():
#     def __init__(self, email): 
#         self.email = email

#     def sign_in(self): 
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email):        
#         super().__init__(email) 
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
# print(wizard1)
# print(dir(wizard1)) #output is: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']
#shows all methods tha the wizard object has. It is useful when we try to figure out what we have access to

#=====================================Dunder Methods============================






