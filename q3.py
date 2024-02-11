def foo(a, b, c, d):
    numbers = [a, b, c, d]
    numbers.sort()
    sum_of_smallest_squares= numbers[0]**2 + numbers[1]**2
    return sum_of_smallest_squares


print(foo(1,2,3,4))
print(foo(-3,1,5,6))
