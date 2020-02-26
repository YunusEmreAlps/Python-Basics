# --------------------
# Example 4 (Strings)

# Y U N U S _ E M R E
# 0 1 2 3 4 5 6 7 8 9
#                  -1

name = "YUNUS EMRE"

print(" -",name[0]) # first character ('Y')
print(" -",name[1]) # second character ('U')
print(" -",name[2]) # third character ('N')
print(" -",name[3]) # fourth character ('U')

print(" -",name[-1]) # last character ('E')
print(" -",name[-2]) # ('R')
print(" -",name[-3]) # ('M')

# ----------
# syntax: (variable_name)[start: stop: step]
#         [:4] -> That means [0:4]
#         [4:] -> That means [4:last index]

print(" -",name[:4]) # "YUNU"
print(" -",name[4:]) # "S EMRE"
print(" -",name[0:3]) # "YUN"
print(" -",name[0:-3]) # "YUNUS_E"
print(" -",name[-4:-1]) # "EMR"
print(" -",name[::2]) # "YNSER"
print(" -",name[::3]) # "YUEE"

# ----------
# methods
# capitalize
# count
# startswith
# endswith  
# find  
# len
# upper
# lower
# title
# format  
# index
# replace
# strip
# split
# isalnum
# isalpha
# isdecimal
# islower
# isupper

# ----------
# variables
tx1="hello world!"
tx2="python programming language"
tx3="mad max Fury Road"

# ----------
# capitalize: converts the first character to upper case 
print(" - tx1 capitalize:",tx1.capitalize()) # Hello world!
print(" - tx2 capitalize:",tx2.capitalize()) # Python programming language
print(" - tx3 capitalize:",tx3.capitalize()) # Mad max Fury Road

# ----------
# count: returns the number of times a specified value occurs in a string
print(" - tx1 'll':",tx1.count('l')) # 3
print(" - tx2 'a':",tx2.count('a'))  # 3  
print(" - tx3 'i':",tx3.count('i'))  # 0

# ----------
# startswith: returns true if string starts with specified value
print(" -",tx1.startswith('A')) # False
print(" -",tx2.startswith('p')) # True  
print(" -",tx3.startswith('m')) # True

# ----------
# endswith: returns true if string ends with specified value
print(" -",tx1.endswith('!')) # True
print(" -",tx2.endswith('a')) # False  
print(" -",tx3.endswith('s')) # False

# ----------
# find: if find this specified value return start index else -1
print(" -",tx1.find("world")) # 6
print(" -",tx2.find("turtle")) # -1
print(" -",tx3.find("max")) # 4

# ----------
# len: returns string length
print(" - tx1 length:",len(tx1)) # 12
print(" - tx2 length:",len(tx2)) # 27
print(" - tx3 length:",len(tx3)) # 17

# ----------
# upper: all character is upper case
print(" - tx1 upper:",tx1.upper()) # HELLO WORLD!
print(" - tx2 upper:",tx2.upper()) # PYTHON PROGRAMMING LANGUAGE
print(" - tx3 upper:",tx3.upper()) # MAD MAX FURY ROAD

# ----------
# lower: all character is lower case 
print(" - tx1 lower:",tx1.lower()) # hello world
print(" - tx2 lower:",tx2.lower()) # python programming language
print(" - tx3 lower:",tx3.lower()) # mad max fury road

# ----------
# title: converts the first character of each word to upper case
print(" - tx1 title:",tx1.title()) # Hello World!
print(" - tx2 title:",tx2.title()) # Python Programming Language
print(" - tx3 title:",tx3.title()) # Mad Max Fury Road

# ----------
# format: formats specified values in a string
tx4="I'm {age:d} years old"
print(" -",tx4.format(age=20)) # hello world

# ----------
# index: searches the string for a specified value and returns the position of where it was found
print(" - tx1",tx1.index('o')) # 4
print(" - tx2:",tx2.index('a')) # 12
print(" - tx3:",tx3.index('R')) # 13

# ----------
# replace: returns a string where a specified value is replaced with a specified value
print(" - tx1:",tx1.replace('h', 'Heeeeee')) # Heeeeeello world
print(" - tx2:",tx2.replace('p', 'P')) # Python programming language
print(" - tx3:",tx3.replace('p', 'TT')) # mad max fury road

# ----------
# strip: removes first spaces and end spaces
tx5= "            KOBE BRYANT           "
print(" -",tx5.strip(),"is LEGEND.") # Kobe Bryant is LEGEND. 


# ----------
# split: splits the string at the specified separator, and returns a list
print(" - tx1 split:",tx1.split()) # ['hello', 'world!']
print(" - tx2 split:",tx2.split()) # ['python', 'programming', 'language']
print(" - tx3 split:",tx3.split()) # ['mad', 'max', 'fury', 'road']

# ----------
# isalnum: if string have alphabetic and numeric character True else False 
tx6 = "Yunus20"
print(" - tx1:",tx1.isalnum()) # False (!)
print(" - tx2:",tx2.isalnum()) # False (_)
print(" - tx6:",tx6.isalnum()) # True

# ----------
# isalpha: if all character is alphabetic True else False
print(" - tx1:",tx1.isalpha()) # False (_)
print(" - tx2:",tx2.isalpha()) # False (_)
print(" - tx6:",tx6.isalpha()) # False (20)

# ----------
# isdecimal: if all character is decimal True else False 

# ----------
# islower: if all character is lower case True else False
print(" - tx1:",tx1.islower()) # True
print(" - tx2:",tx2.islower()) # True
print(" - tx3:",tx6.islower()) # False

# ----------
# isupper: if all character is upper case True else False
print(" - tx1:",tx1.isupper()) # False
print(" - tx2:",tx2.isupper()) # False 
print(" - tx5:",tx5.isupper()) # True
