# def factorial(n):
#     if n < 0:
#         raise ValueError("El factorial no está definido para números negativos.")
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Prueba de la función
# print(factorial(5))  # Resultado: 120

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(3)) # Resultado: 5    
