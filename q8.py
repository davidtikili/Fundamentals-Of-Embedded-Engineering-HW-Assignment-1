def double_5(n):
    strings = str(n)
    for i in range(len(strings) - 1):
        if strings[i:i+2] == '55':
            return True
    
    return False
print(double_5(5))    
print(double_5(55))       
print(double_5(550055))   
print(double_5(12345))    
print(double_5(50505050)) 