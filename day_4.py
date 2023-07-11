
# Online Python - IDE, Editor, Compiler, Interpreter

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
arr = [3,4,1,-3,2,0]        
print(min_positive(arr))
   
    
            
