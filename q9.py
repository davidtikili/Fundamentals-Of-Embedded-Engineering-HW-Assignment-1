def uniq_digits(x):

    input_digits = str(x)
    
    unique_digits = set()
    
    for digit in input_digits:
        unique_digits.add(digit)
    
    return len(unique_digits)
print(uniq_digits(8675309))    
print(uniq_digits(1313131))    
print(uniq_digits(13173131))   
print(uniq_digits(10000))      
print(uniq_digits(101))        
print(uniq_digits(10))         
