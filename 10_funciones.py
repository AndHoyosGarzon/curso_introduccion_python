### Funciones ###
# son bloques de codigo que cumplen una trabajp especifico o resuelve un problema en concreto

def my_function():
    print("esto es una funcion")           

def sum_two_values(a, b):
    if type(a) == int and type(b) == int:
        print(a + b)
    else: 
        print("El tipo de dato ingresado no es valido")


def sum_two_values_with_return(a, b):
    if type(a) == int and type(b) == int:
        return(a + b) # retornamos datos de la funcion
    else: 
        return("El tipo de dato ingresado no es valido")

my_result = sum_two_values_with_return(8, 10) # almacenamos el retorno de la funcion en una variable 
print(my_result)

def print_name(name, surname):
    print(f"mi nombre es {name} {surname}")

print_name(surname = "felipe", name = "andres")




