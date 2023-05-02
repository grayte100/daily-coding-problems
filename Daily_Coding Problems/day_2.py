#Given an array of integers, return a new array such that each element at index i of 
#the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
#[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].


import math
def arrary_product(my_list):
    j = 0
    i = 1
    arr = []
    for j in range(0,len(my_list)):
        b = [element for element in my_list if element != my_list[j]]
        #if element != my_list[j]:
        arr.append(math.prod(b))
        j += 1
           
    print(arr)

print()
