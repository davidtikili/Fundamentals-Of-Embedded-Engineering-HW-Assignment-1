def sum_of_proper_divisors(num):
    divisor_sum = 1 
    j = int(num**0.5)
    for i in range(2, j + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num//i: 
                divisor_sum += num//i
    
    return divisor_sum

def amc(n):
    num = n + 1
    
    while True:
        sum_divisors = sum_of_proper_divisors(num)
        sum_divisors1 = sum_of_proper_divisors(sum_divisors)
        
        if num != sum_divisors and num == sum_divisors1:
            return num
        
        num += 1
print(amc(5))    
print(amc(220))  
print(amc(284))  
r = amc(5000)
print(r)