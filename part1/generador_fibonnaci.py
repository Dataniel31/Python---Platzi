def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a+b
    
for value in fibonacci(10):
    print(value)