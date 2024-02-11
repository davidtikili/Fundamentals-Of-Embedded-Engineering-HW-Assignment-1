def pfct_num(n):
    if n <= 1:
        return False
    
    sum_of_factors = 1  
    j = int(n**0.5)
    for i in range(2, j + 1):
        if n % i == 0:
            sum_of_factors += i
            if i != n//i:  
                sum_of_factors += n//i
    
    return sum_of_factors == n
print(pfct_num(6))   
print(pfct_num(8))   
print(pfct_num(28))  