# List

student_1 = 78
student_2 = 80
student_3 = 43
student_4 = 65
student_5 = 90

# Non-Scalar
grades = [
    student_1, 
    student_2,
    student_3,
    student_4,
    student_5]

print(grades)

print(grades[0]) # 78
print(grades[1]) # 80
print(grades[2]) # 43
print(grades[3]) # 65
print(grades[4]) # 90


arr = [1, 2, "a", "b", True, 4.5, [1,2,3]]
print(arr)

# ---------- Indexing & Slicing ----------
print(grades[0]) # 78
print(grades[-1]) # 90
# print(grades[10]) # IndexError
print(grades[1:]) # [80, 43, 65, 90]
print(grades[1:3]) # [80, 43]
print(grades[:200]) # [78, 80, 43, 65, 90]
print(grades[:3000])  # [78, 80, 43, 65, 90]

grades[1] += 5
print(grades)

# ---------- Mutable ----------
arr = [1, 2, 3, 4]
print(arr[0:3]) # [1, 2, 3]

arr[0:3] = [30, 40, 50]
print(arr)

arr = [1, 2, 3, 4]
arr[0:3] = [30, 40]
print(arr)

arr = [1, 2, 3, 4]
arr[0:3] = [30]
print(arr)

# ---------- len() ----------
print(len(arr)) # 2
print(len(grades)) # 5

# ---------- append() ----------
arr = [1, 2, 3]
arr.append(200)
print(arr) # [1, 2, 3, 200]

# ---------- extend() ----------
arr = [1, 2, 3]
arr.extend([100, 200, 300])
print(arr) # [1, 2, 3, 100, 200, 300]

# ---------- insert() ----------
arr = [1, 2, 3, 4 ,5]
arr[0] = 100
print(arr) # [100, 2, 3, 4, 5]

arr = [1, 2, 3, 4 ,5]
arr.insert(0, 100)
print(arr) # [100, 1, 2, 3, 4, 5]
arr.insert(3, 44)
print(arr) # [100, 1, 2, 44, 3, 4 , 5]

# ---------- remove() ----------
arr = [1, 2, 3, 40, 30, 40]

try: 
    arr.remove(40)
except ValueError:
    pass

print(arr)

# ---------- pop() ----------
arr = [1, 2, 3, 4, 5, 6]
print(arr.pop(1)) 
print(arr) # [1, 3, 4, 5, 6]

arr = [1, 2, 3, 4, 5, 6]
print(arr.pop(1) + 4) # 6
print(arr) # [1, 3, 4, 5, 6]

# arr.pop(100) # IndexError

# ---------- count() ----------
arr = [1, 2, 44, 4, 5, 1]
print(arr.count(1)) # 2
print(arr.count(44)) # 1
print(arr.count(1000)) # 0

# ---------- Aliasing ----------
a = 2
b = a

print(a) # 2
print(b) # 2

a += 1 

print(a) # 3
print(b) # 2

arra = [1, 2, 3]
arrb = arra

print(arra) # [1, 2, 3]
print(arrb) # [1, 2, 3]

arra[0] = 200

print(arra) # [200, 2 , 3]
print(arrb) # [200, 2 , 3]

# ---------- copy() ----------
arrb = arra.copy()

print(arra) # [200, 2, 3]
print(arrb) # [200, 2, 3]

arra[0] = 300

print(arra) # [300, 2 , 3]
print(arrb) # [200, 2 , 3]

# ---------- concatination ----------
arra = [1, 2, 3]
arrb = [4, 5, 6]

print(arra) # [1, 2, 3] 
print(arrb) # [4, 5, 6]

print(arra+arrb) # [1, 2, 3, 4, 5, 6]

# ---------- index() ----------
arr = [1, 2, 3, 4, 3, 5, 6]

print(arr.index(3)) # 2
print(arr.index(4)) # 3

# ---------- reverse() ----------
arr = [1, 2, 3, 4]

arr.reverse() # [4, 3, 2, 1]
print(arr[::-1]) # [1, 2, 3, 4]

# ---------- sort() & sorted() ----------
arr = [1, 2, 3, 4]

arr.reverse() # [4, 3, 2, 1]
print(arr[::-1]) # [1, 2, 3, 4]



l = [[1,-20,3], [2,-200,-3]]
l.sort()
print(l)

l = [[2, -2, 3], [10, -20, -3]]
l.sort()
print(l)
