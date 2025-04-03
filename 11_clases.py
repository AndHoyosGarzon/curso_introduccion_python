### Clases ###
## nos da la capacidad de definir un objeto de la vida real pero con codigo

class MyEmptyPerson: #forma predeterminada de definir una clase
    pass # no retorna nada

#print(MyEmptyPerson) #<class '__main__.MyEmptyPerson'>

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    # agregando metodos y funciones a una clase constructora
    def walk(self):
        print(f"{self.full_name} Esta caminando")
        
new_person = Person("andres", "hoyos")

new_person.walk()