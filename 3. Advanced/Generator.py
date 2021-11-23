# Generators

def square(arr):
    res = []
    
    for i in arr:
        res.append(i**2)
    
    return res


arr =  [1, 2, 3, 4, 5]
square(arr)

def square_generator(arr): 
    for i in arr:
        yield i**2
    



arr =  [1, 2, 3, 4, 5]
g = square_generator(arr)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))