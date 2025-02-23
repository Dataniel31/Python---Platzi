class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")
        

persona = Person("DANIEL", 23)
persona.greet()