#Assuming only non-negative integers as input
n = int(input("What number do you want to find it's factorial?"))

def fact(n):
    if n >= 1:
        return (n * fact(n-1))
    else:
        return 1
    
print ("{} factorial = ".format(n), fact(n))


#Fibonacci series

n = int(input("Enter the term of the fibonacci series you want to find"))
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
    
print ("the fibonacci series at position {} is: ".format(n), fib(n))


#Staricase/frog problem
#find the number of ways to take one of two steps to get to the top of a staircase
n = int(input("Enter the number of steps: "))
def num_ways(n):
    if n ==0:
        return 1
    elif n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)
    
print("number of ways to use one or two steps for {} number of stairs is: ".format(n), num_ways(n))


#using dynamic programming to save space and increase runtime speed
n = int(input("Enter the number of steps: "))
def num_ways_bottoms_up(n):
    if n ==0 or n==1: return 1
    nums = []
    for i in range(n):
        nums.append(i+1)
    nums[0] = 1; nums[1] = 1
    for i in range (2,n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]
print("number of ways is: ", num_ways_bottoms_up(n))
    