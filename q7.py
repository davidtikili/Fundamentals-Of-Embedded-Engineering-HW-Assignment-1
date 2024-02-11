def same_ord(a, b):
    number_of_bits_a = len(str(a))
    number_of_bits_b = len(str(b))
    
    return number_of_bits_a == number_of_bits_b
print(same_ord(50, 70))        
print(same_ord(50, 100))      
print(same_ord(1000, 100000))  