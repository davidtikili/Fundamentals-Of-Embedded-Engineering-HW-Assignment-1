def sum_odd(n):
    sum = 0
    for i in range(1,n+1,2):
        sum += i
    return sum

print(sum_odd(6))
print(sum_odd(7))
        
        