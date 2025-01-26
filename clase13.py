numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers[2])
information = {"nombre": "Daniel",
               "apellido": "Suclle", 
               "altura" : 1.70, 
               "edad" : 22}
print(information)
del information["edad"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)
print(type(values))


items = information.items()
print(items)
print(type(items))

