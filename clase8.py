# Operadores Numéricos
a = 10
b = 3

print("Suma: ", a + b)
print("Resta: ", a - b)
print("Multiplicación: ", a * b)
print("División: ", a / b)

print("División entera: ", a // b)	# División entera
print("Módulo: ", a % b)	# Resto de la división
print("Potencia: ", a ** b)	# Potencia

a += 2
a -= 2
a *= 2
a /= 2
print(a)

# Jerarquia  PEMDAS (Parentesis, Exponentes, Multiplicación, División, Adición, Sustracción)

operation_1 = 3 + 2 * 5
operation_2 = (3 + 2) * 5
print(operation_1)
print(operation_2)

operation_3 = (2+3)*(4**2)/ 8 - 1
print(operation_3)