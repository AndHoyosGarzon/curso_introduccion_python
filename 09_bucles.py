### Loops ###

# While => Se ejecuta mientras la condicion se cumpla 
my_condition = 10
while my_condition < 10:
    print(my_condition )
    my_condition += 1
else: 
    print(f"Aqui por fin termino ya que la variable equivale a {my_condition}")
    #se ejecuta mientras my_condition no sea igual a 10

#print("=================================================================")
while my_condition >= 10 and my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print(f"mi variable ahora tiene el numero: {my_condition}")
        break # sale del loop cuando estamos en el numero 15
    print(my_condition)


# FOR => se ejecuta mientras cumplamos una condicion especifica se utiliza mas que nada para recorres listas o arrays
print("==================================BUCLE FOR===============================================")
my_list = [10, 20, 30, 40, 50]
for element in my_list: # reccorriendo una lista
    if element == 30:
        print(f"ahora llegamos al numero que buscamos: {element}")

my_tuple = ("andres", "felipe", "hoyos", "garzon", 33)
for element in my_tuple: # recorriendo una tupla
    print(element)

my_set = {"mama", "papa", "esposa", "hijo"}
for element in my_set: # recorriendo un set
    print(element)

my_dict = {"nombre":"andres", "apellido": "Hoyos", "rut": "24.926.549-7"}
for element in my_dict: # recorriendo un diccionario
    print(f"los datos son los siguientes {element} ")
