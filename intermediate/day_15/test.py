def fact(num):
    
    
    fact_result = num * fact(num-1)

    if num < 1:
        return fact_result

print(fact(5))