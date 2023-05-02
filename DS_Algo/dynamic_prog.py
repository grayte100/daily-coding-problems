def fib(n, memo):
    if memo[n] != None: #Simply put, it asks if the particular fib term has been found before
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = (fib((n-1), memo) + fib((n-2), memo))
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1) #creating an empty list of size n+1
    return fib(n, memo)

n = int(input("Enter the sought term of the Fibonacci series: "))

print(fib_memo(n))


def fib_bottoms_up(n):
    if n == 1 or n == 2:
        return 1
    bottoms_up = [None] * (n+1)
    bottoms_up[1] = 1
    bottoms_up[2] = 1
    for i in range (3, n+1):
        bottoms_up[i] = bottoms_up[i-1] + bottoms_up[i-2]
        
    return bottoms_up[n]

print(fib_bottoms_up(n))
    
    
