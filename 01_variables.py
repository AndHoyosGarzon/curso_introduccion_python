# creando variables en python
my_str_variable = "Esta es mi varible"
print(my_str_variable)

my_int_variable = 12343
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print 
print(my_str_variable, my_int_to_str_variable, my_bool_variable)

# algunas Funciones del sistema
print(len(my_str_variable)) # 18

# Declarando Variables en una sola linea, tener en cuenta que esto es una mala practica
name, surname, alias, age = "andres", "Hoyos", "pipe", 33
print("Mi nombre es: ", name,surname, " mis amigos me conocen como, ", alias, " y tengo ", age, " años.")

#input ingreso de datos para usuarios por medio de la consola
first_name = input("what is your name ?")
year_old = input("How old are you ?")
print("Nombre: ", first_name, " edad: ", age)

#forzando el tipo de dato 
address: str = "mi direccion"
address = 32
print(address)
print(type(address))

