try:
    divisor = int(input("Ingresa un numero divisor : "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Ha ocurrido un error",e)
except ValueError as e:
    print("Error : Debes ingresar un numero")
    print("Error : ", e)