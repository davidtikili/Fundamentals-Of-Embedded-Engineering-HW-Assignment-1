def df(a, b, c):
    if a - b == c or a - c == b:
        return True
    elif b - a == c or b - c == a:
        return True
    elif c - a == b or c - b == a:
        return True
    else:
        return False

print(df(5, 3, 2))   
print(df(2, 3, 5))   
print(df(2, 5, 3))   
print(df(-2, 3, 5))  
print(df(-5, -3, -2))
print(df(-2, 3, -5)) 
print(df(2, 3, -5))  
print(df(10, 6, 4))  
print(df(10, 6, 3))  