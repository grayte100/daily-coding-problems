
#Good morning! Here's your coding interview problem for today.

#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def two_sum(my_list, sought_sum):
    
    sub_lists = []
    j = 0
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list)):
            if i !=j: 
                sub_lists.append([my_list[j] + my_list[i]])
    print(sub_lists)

    b = [x for x in sub_lists]
    c = [x for x in b if (sum(x) - sought_sum == 0)]
    if len(c) > 0:
        return True
    else:
        return False
    
    


print (two_sum([3,5,7,11,13], 24))
        
        
    
        
    