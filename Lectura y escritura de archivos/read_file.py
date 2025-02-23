#Leer un archivo linea por linea
"""with open("caperucita.txt",'r') as file:
    for lineas in file:
        print(lineas.strip)"""
        
#Leer todas las lineas pero en una lista
"""with open("caperucita.txt", 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Añadir informacion
"""with open("caperucita.txt", 'a') as file:
    file.write("\n\nBy:ChatGPT")"""
    
    
#Sobreescriir el texto
# with open("caperucita.txt", 'w') as file:
#     file.write("\n\nBy:ChatGPT")

with open("caperucita.txt",'r') as file:
    lines = file.readlines()
    print(len(lines))


    