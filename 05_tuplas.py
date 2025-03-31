### Tuplas ###
my_tuple = tuple() # constructor de tupla 
my_other_tuple = () # constructor de tupla

my_tuple = (35, 1.75, "andres", "Hoyos")
print(my_tuple)
print(type(my_tuple)) # class tuple
print(my_tuple[0]) # 35
print(my_tuple[-1]) # Hoyos

### operaciones del sistema para las tuplas ###
print(my_tuple.count(35)) # cuenta las coinsidencias encontradas en la tupla
print(my_tuple.index(1.75)) # nos encuentra en que indice esta el elemento que solicitamos como parametro


## recordar que las tuplas son estructuras de datos inmutables.....
