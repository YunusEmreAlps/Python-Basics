# Args & Kwargs



# --------- *args ---------
# Degişken sayılı parametre vermenin bir yoludur. List/Tuple objelerini unpack yapar ama dictionary objelerini yapmaz
def sum(numbers):
    total = 0
    
    for i in numbers:
        total += i
    
    return total

print(f"Total: {sum([1, 2, 3, 4])}")

# *arg'ın anlamı en başta tuple gibi bir objem vardı ama ben bunu tek tek elemanlarına ayırdım demek.

def sum(*args):
    total = 0
    
    print(type(args)) # tuple
    print(args)       # (1, 2, 3, 4)
    
    
    for i in args:
        total += i
        
    return total

print(f"Total: {sum(1, 2)}")                    # 3
print(f"Total: {sum(1, 2, 3, 4)}")              # 10
print(f"Total: {sum(1, 2, 3, 4, 5)}")           # 15
print(f"Total: {sum(1, 2, 3, 4, 5, 6)}")        # 21
print(f"Total: {sum(1, 2, 3, 4, 5, 6, 7)}")     # 28
print(f"Total: {sum(1, 2, 3, 4, 5, 6, 7, 8)}")  # 36


def sum2(*args):
    total = 0
    
    print(type(args)) # tuple
    print(args)       # (1, 2, 3, 4)
    
    
    for i in args:
        for j in i:
            total += j
        
    return total

print(f"Total: {sum2([1, 2, 3, 4])}")  # 10


# --------- **kwargs ---------
# Fonksiyona değişken sayıda keyword argument verebilmemi sağlar.
def students(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


students(name = "Yunus Emre", age = 21)


# --------- Using *args and **kwargs together ---------
def weird(*args, **kwargs):
    total = 0
    
    for i in args:
        total += i
        
        
    for k, v in kwargs.items():
        print(f"{k} : {v}")   
        
    return total

print(weird(1, 2, 3, 4, 5, 6, 7, 8, 9, name = "Yunus Emre", age = 21))

# --------- Unpacking ---------
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [10, 11, 12, 13, 14, 15, 16] 

print(*arr) # 1, 2, 3, 4, 5, 6, 7, 8, 9

merged_list = [*arr, *arr2]
print(merged_list)


dict1 = {"name": "Yunus Emre", "age": 21}
dict2 = {"name": "Mahmut", "surname": "Alpu"}
dict3 = {"name": "Beduk", "surname": "Koray"}

dict4 = {**dict1, **dict2}
print(dict4)


myname = "Yunus Emre Alpu"

name = [*myname]
print(name)
