# --------------------
# Example 2 (Input)

# if you want to interactive program 
# you need to use "input" instruction

# syntax:
# input(" - Please enter your name ")
# input(' - How old are you : ')

input(" - What's your name : ")
input(" - How old are you : ")


# ----------
# you need to put your data in variable 
# if we not put this data(for example: your name)
# everytime we need to use 'input' instruction for same data

name = input(" - What's your name : ") # Variable

# , 
print(" - Your name is",name) # Your name is ...

# + 
print(" - Your name is"+name) # Your name is...
print(" - Your name is "+name) # Your name is ...
print(" - Your","name","is",name) # Your name is ...

# formatting 
print(f" - Your name is {name}") # Your name is ...


print(" - Python is very powerful Language.")
print(" -","Pyhton","is","very","powerful","language")
print(" - "+"Python"+"is"+"very"+"powerful"+"language")

# ---------- 
# data           type
# Yunus Emre -> string
# 15         -> integer
# 3.15       -> float 
# PI number  -> long
# True       -> boolean   

# !! ALL INPUTS ARE STRING !!
age = input(" - How old are you : ")
print(f" - Hello, I'm {name}. \n - I'm {age} years old.")

print(" -",type("Yunus Emre"))
print(" -",type(name))
print(" -",type(age))
print(" -",type(20))
print(" -",type(11.45)))
print(" -",type(True))

# ----------
# print(age+5) # type error : can only concatenate str (not "int") to str
print(" -",age+" is not string")

# ----------
age = int(age) # type conversion (string -> age)
print(f" - result : {age+5}") 


surname = "Alpu" # string 
weight = 80 # int
height = 1.86 # float
is_student = True # boolean

print(f" - My last name is {surname}.\n - My height is {height}.\n -  My Weight is {weight}.\n - Student:{is_student}")



