to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar el museo",
         "Volver al hotel"]

print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))

mix = ["uno", 2 , 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print("Primer elemento :",mix[0])
print("Último elemento :",mix[-1])

string = "Hola Mundo"
print("Primer elemento :",string[0])
print("Último elemento :",string[-1])
print(mix[2:-2])
print(mix)
mix.append("False")
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1,["a", "b"])
print(mix)

print(mix.index(["a", "b"]))

numbers = [100, 200.0, 3, 4, 5]

print("Mayor:", max(numbers))
print("Mayor:", min(numbers))

del numbers[-1]
print(numbers)