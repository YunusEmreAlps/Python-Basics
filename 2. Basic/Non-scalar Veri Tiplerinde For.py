# Non-Scalar For

# --------- List ---------
grades = [90, 72, 81, 77]

for i in grades:
    print(i)
# 90 
# 72 
# 81 
# 77

total = 0

for i in grades:
    total += i

average = (total / (len(grades)))
print("Average: "+str(average))


for i in range(len(grades)):
    print("Iteration :"+str(i))

print(grades) # [90, 72, 81, 77]    
for i in range(len(grades)):
    grades[i] += 5
    
print(grades) # [95, 77, 86, 82]

# (Continue)
grades = [90, 72, 81, 77]

print(grades) # [90, 72, 81, 77]    
for i in range(len(grades)):
    print(grades[i])
    if(i == 1):
        continue
    
    grades[i] += 5
    
print(grades) # [95, 72, 86, 82]

# (Break)
user = int(input("Number: "))

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(nums)):
    print(nums[i])
    if(nums[i] == user):
        print("Found it!")
        break
    
    
print(nums) # [95, 72, 86, 82]

# --------- Tuple ---------

tList = (1, 2, 3, 4)

for i in tList:
    print(i)

# 1
# 2
# 3
# 4

total = 0

for i in tList:
    total += i
    
print(total) # 10

total = 0

for i in range(len(tList)):
    total += tList[i]
    
print(total) # 10

# --------- Dictionary ---------

students = {
    "student_1": [90,89], 
    "student_2": [80,83], 
    "student_3": [72,71]
}
    
for i in students:
    print(i)
    
# student_1
# student_2
# student_3
    
for i in students:
    print(students[i])

# [90, 89]
# [80, 83]
# [72, 71] 
    
for i in students.values():
    print(i)
    
# [90, 89]
# [80, 83]
# [72, 71]     
    
students = {
    "student_1": 90, 
    "student_2": 80, 
    "student_3": 72
}    
    
for i in students:
    if(students[i] > 85):
        print(i)
    
for k, v in students.items():
    print("Key: "+str(k)+", Value: "+str(v))
    
    
    
    