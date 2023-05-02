#Given an array of integers, find the first missing positive integer in linear time and 
# constant space. In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3##


def min_positive(arr):
    if sum(arr) <= 0:
        return 1
    a = [i for i in arr if i>0]
    b = [x for x in range(1, (max(a)+2))]
    if min(a) > 1:
        return 1 
    else:
        complement_set = set(b) - set(a)
        return min(complement_set)
arr = [0,1,-2,4,7,8]        
print(min_positive(arr))