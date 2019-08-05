def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        i += 1
    return result   
    
fact(5)