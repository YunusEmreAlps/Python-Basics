# PROJECT

flat_list = []
    
# Q1: Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]
def solution1(arr):
    # iterating over the data
    for i in arr:
        # checking for list
        if(type(i) == list):
            solution1(i)
        else:
            flat_list.append(i)
    pass


# Q2
# input :  [[1, 2], [3, 4], [5, 6, 7]] 
# output : [[7, 6, 5], [4, 3], [2, 1]]
def solution2(arr):
    reverse_list = list()
    
    for i in range(len(arr)-1, -1, -1):
        temp = list()
        for j in range(len(arr[i])-1, -1, -1):
            temp.append(arr[i][j])
        reverse_list.append(temp)
    return reverse_list
    pass
 


arr1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
arr2 = [[1, 2], [3, 4], [5, 6, 7]]                 

solution1(arr1)
print(flat_list)
print(solution2(arr2))



