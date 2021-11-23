# --------------------
# Example 3 (Arithmetic Operators)

# + : Addition 
# - : Subtraction 
# * : Multiplication 
# / : Division 
# % : Module 
# ** : Exponential notation

num1 = float(input(" - Enter first number : "))
num2 = float(input(" - Enter second number : "))

print(f" - {num1} + {num2} = {num1+num2}") # Addition
print(f" - {num1} - {num2} = {num1-num2}") # Subtraction
print(f" - {num1} * {num2} = {num1*num2}") # Multiplication
print(f" - {num1} / {num2} = {num1/num2}") # Division
print(f" - {num1} % {num2} = {num1%num2}") # Module
print(f" - {num1}^2 = {num1**2}") # Exponential notation
print(f" - {num2}^2 = {num2**2}") # Exponential notation
print(f" - {num1}^{num2} = {num1**num2}") 
print(f" - {num2}^{num1} = {num2**num1}") 

# Operator precedence:
# 1. parenthesis
# 2. exponentiation
# 3. multiplication, division
# 4. addition, subtraction

# ---------- 
print(6*4+2)   # 26
print(6*4-2)   # 22
print(6*4*2)   # 48
print(6*4/2)   # 12.0

print(6/4+2)   # 3.5
print(6/4-2)   # -0.5
print(6/4*2)   # 3.0
print(6/4/2)   # 0.75
 
print(6+4+2)   # 12
print(6+4-2)   # 8
print(6+4*2)   # 14 
print(6+4/2)   # 8

print(6-4+2)   # 4
print(6-4-2)   # 0
print(6-4*2)   # -2
print(6-4/2)   # 4.0

print(6*(4+1)) # 30
print(6/(4+1)) # 1.2
print(6+(4+1)) # 11
print(6-(4+1)) # 1

# ----------
res = (num1+num2)*num1 / num2
print(f" - Result : {res}")

# num1 = num1+10 or num1 += 10
# num1 = num1-10 or num1 -= 10
# num1 = num1*10 or num1 *= 10
# num1 = num1/10 or num1 /= 10

num1+=10
print(" -",num1)
num1-=5
print(" -",num1)
num1/=6
print(" -",num1)
num1*=2
print(" -",num1)

# ---------- 
num=5
print(" -",float(num)) # 5.0
num=5.7
print(" -",int(num)) # 5
num=7
print(" -",complex(num)) # 7+0j