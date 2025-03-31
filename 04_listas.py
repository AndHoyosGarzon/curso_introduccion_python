### Listas ó Arrays ###
my_list = list()
my_other_list = []

#print(len(my_list)) # Longitud 0

my_list = [33, 35, 30, 52, 30, 17]
#print(len(my_list))

my_other_list = [35, 1.75, "Andres", "Hoyos"]
#print(type(my_other_list))

#print(my_other_list[0])
#print(my_other_list[1])
#print(my_other_list[-1])
#print(my_other_list[-2])
#print(my_list.count(30))

# igualamos variables en una linea a los datos de una lista 
#age, height, name, surname = my_other_list
#print(age, name, surname, height)

# concatenando listas
#print(my_list + my_other_list) # [33, 35, 30, 52, 30, 17, 35, 1.75, 'Andres', 'Hoyos']


### Agregando elementos a una lista por medio de metodos propios de las listas ###
my_other_list.append("garzon") # agrega al final
my_other_list.insert(0, "azul") # inserta datos en el indice especificado en el primer parametro
my_other_list.remove("Andres") # elimina el dato ingresado por parametro si encuentra una coincidencia en caso de no encontrar da error
my_other_list.pop() # elimina el ultimo elemento de la lista en este caso es el apellido garzon y se puede almacenar este valor en una variable
del my_other_list[3] # elimina el dato ubicado en el indice ingresado 
#my_other_list.clear() # limpia toda la lista vacia []

my_other_list[1] = "amarillo" # reasignamos el tipo de dato ubicado en la posicion especifica

my_new_copy_list = my_other_list.copy() # creamos una copia exacta de la lista
my_new_copy_list.reverse() # dandole la vuelta a la lista 
print(my_new_copy_list) # [1.75, 'amarillo', 'azul']

my_list_int = [10, 9, 8, 7] 
my_list_int.sort() # ordena dependiendo el orden que le asignemos
print(my_list_int) #[7, 8, 9, 10]






















