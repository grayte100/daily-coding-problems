def sum_numbers(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return (n + sum_numbers(n-1))
    
print(sum_numbers(100))


