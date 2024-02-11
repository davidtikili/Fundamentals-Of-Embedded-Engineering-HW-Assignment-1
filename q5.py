def lrgst_factor(m):
    largest_factor = 1  
    for num in range(2, m//2 + 1):
        if m % num == 0:
            largest_factor = num 
    
    return largest_factor

print(lrgst_factor(15))   
print(lrgst_factor(80))   
