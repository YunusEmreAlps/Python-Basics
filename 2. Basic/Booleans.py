# --------------------
# Example 5 (Booleans)

# > left operand is greater than the value of right operand
# < left operand is lower than the value of right operand
# == equal 
# != not equal
# or : least one of two statements is True.
# and : two statements is True

print(10>9) # True
print(10==9) # False
print(10<9) # False
print(bool("abc")) # True
print(bool(0)) # False
print((4==4) or (10==9)) # True
print((4==4) and (10==9)) # False
print((4==4) and (10==10)) # True
print((4==9) or (10==9)) # False