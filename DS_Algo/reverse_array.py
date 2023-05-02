def reverseArray(a):
    # Write your code here
    n = 0
    integer_array = []
    for i in a:
        integer_array.append(a[(len(a)-1)-n])
        n += 1
    return integer_array
print (reverseArray([3,4,5,68]))