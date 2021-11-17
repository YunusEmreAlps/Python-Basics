# List Comprehensions
squares = []

for i in range(1, 11):
    squares.append(i*i)
    
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = [i*i for i in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def cube(x):
    return x**3
    
cubes = [cube(i) for i in range(1, 11)]
print(cubes)

# --------- Conditional ---------
print(squares)

odd_squares = []

for i in range(len(squares)):
    # Odd Number
    if(squares[i] % 2 == 1):
        odd_squares.append(squares[i])
        
print(odd_squares) # [1, 9, 25, 49, 81]

odd_squares = [i for i in squares if i % 2 == 1]
print(odd_squares) # [1, 9, 25, 49, 81]


def is_odd(x):
    if x % 2 == 0:
        return False
    else: 
        return True
    
odd_squares = [i for i in squares if is_odd(i)]
print(odd_squares) # [1, 9, 25, 49, 81]

# Empty List 
def empty(x):
    if x % 2 == 0:
        return False
    else: 
        return False
    
empty_squares = [i for i in squares if empty(i)]
print(empty_squares) # []

# Even Number
def is_even(x):
    if x % 2 == 0:
        return True
    else: 
        return False
    
even_squares = [i for i in squares if is_even(i)]
print(even_squares) # [4, 16, 36, 64, 100]


# Weird Squares
weird_squares = [i if i%2 == 0 else -1 for i in squares]
print(weird_squares)
# [-1, 4, -1, 16, -1, 36, -1, 64, -1, 100]


ultra_weird_squares = [i if i%2 == 0 else -1 for i in squares if is_even(i)]
print(ultra_weird_squares) 
# [4, 16, 36, 64, 100]


# --------- Set ---------

numbers = [1,2,3,4,5,6,7,1,2]

set_numbers = {i for i in numbers if(i in numbers)}

print(set_numbers)

# --------- Dictionary ---------

square_dict = {i: i**2  for i in range(1, 11)}

print(square_dict)
print(square_dict[9])


# --------- Nested List Comprehension

matrix = [[j for j in range(7)] for i in range(5)]

print(matrix)

matrix = [[10, 11, 12], [13, 14], [15, 16, 17, 18]] 

for i in matrix:
    print(i)

new_matrix = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        new_matrix.append(matrix[i][j])
        
print(new_matrix)
# [10, 11, 12, 13, 14, 15, 16, 17, 18]
    

flatten_matrix = [j for i in matrix for j in i]

print(flatten_matrix)

flatten_matrix = [j for i in matrix for j in i if j%2 == 0]

print(flatten_matrix)


matrix =[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]

flatten_matrix = [k for i in matrix for j in i for k in j]

print(flatten_matrix)

