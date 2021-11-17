# Enumerate

# --------- enumerate() ---------

users = ["Yunus", "Emre", "Mahmut"]

for i in users:
    print(i)
# Yunus
# Emre
# Mahmut
    
for i in range(len(users)):
    print(users[i])
# Yunus
# Emre
# Mahmut

x, y = (4, 5)
print(x) # 4
print(y) # 5

arr = [(1,2), (10,20)]

for i in arr:
    print(i)
# (1, 2)
# (10, 20)

for i in arr:
    a, b = i
    print(a)
    print(b)
    
    
for a, b in arr:
    print("Tuple[0]: ", a)
    print("Tuple[1]: ", b)
    
# Tuple[0]: 1
# Tuple[1]: 2
# Tuple[0]: 10
# Tuple[1]: 20
    
names = ['Tyler', 'Blake', 'Cory', 'Cameron']
    
for i, j in enumerate(names):
    print(i, "My name is ", j)
    
# 0. My name is Tyler
# 1. My name is Blake
# 2. My name is Cory
# 3. My name is Cameron

for i, j in enumerate(names, start=100):
    print(i,"My name is ", j)
    
# 100. My name is Tyler
# 101. My name is Blake
# 102. My name is Cory
# 103. My name is Cameron
    
# --------- zip() ---------

users = ["Yunus", "Emre", "Mahmut"]
grades = [90, 100, 50]

for i, j in zip(users, grades):
    print(i, j)
    
for i in zip(users, grades):
    print(i)
    
for i in range(len(users)):
    print(users[i], grades[i])
    
keys = ['Name', 'Surname', 'Country', 'job']
values = ['Yunus Emre', 'Alpu', 'Turkey', 'Computer Engineer']

dict = {}

for i in range(len(keys)):
    dict[keys[i]] = values[i]
    
print(dict)

dict = {}

for i, j in zip(keys, values):
    dict[i] = j
    
print(dict)

    

