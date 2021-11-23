# --------------------
# Example 1 (Output)

# This is comment

"""
This
is
multi-line
comments
"""

# if you want to show something on console
# you need to use a "print" instruction 

# syntax:
# print('Message') -> single quotes
# print("Message") -> double quotes

print(' - Hello World!')
print(" - I love Python programming language.")

# ----------
# print('I'm Yunus Emre') syntax error
print(" - I'm Yunus Emre")
print(" - I'm student of computer engineer.")

# ----------
# print("George always says "I love you"") syntax error
print(' - George always says "I love you"')
print(' - “Be the change that you wish to see in the world.” Mahatma Gandhi')

# ----------
# Escape sequence syntax : 
# \n -> new line
# \t -> tab
# \r -> return  
# \\ -> backslash 

# ----------
print(" - first line \n") 
print("\n - second line")
# first line 
# (new line)
# (new line)
# second line

# ----------
print(" - A \t B \t C \n")

# ----------
# This is important 
# _-_Avatar (return)
# _-_James
# Output : Jamesr
print(" - Avatar \r - James") 
print("\t\t Escape Sequence\r - Python") 

# ----------
# print("\") syntax error
print(" - \\")

# ----------
# if you want to read a paragraph you need to use: 
print(''' - If you choose to use your status and influence to raise your voice on behalf of those who have no voice; if you choose to identify 
 not only with the powerful, but with the powerless; if you retain the ability to imagine yourself into the lives of those who do not 
 have your advantages, then it will not only be your proud families who celebrate your existence, but thousands and millions of 
 people whose reality you have helped change. We do not need magic to change the world, we carry all the power we need inside 
 ourselves already: we have the power to imagine better.
      ''')

# ----------
print("+"*10) # Output:++++++++++