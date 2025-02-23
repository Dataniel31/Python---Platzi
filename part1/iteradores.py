
my_list = [1, 2, 3, 4]

my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


text = "Hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)