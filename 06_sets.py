### Sets ###
### Un set no es una estructura ordenada
### Un set no admite datos repetidos

my_set = set() # funcion constructora
my_other_set = {}

print(type(my_set)) #<class 'set'>
print(type(my_other_set)) #<class 'dict'>

my_other_set = {"andres", "felipe", 33}
print(type(my_other_set)) #<class 'set'>

my_other_set.add("aepe")
print(my_other_set)

# sintaxis para verificar un dato dentro de un set
print("andres" in my_other_set) # true
print("juanito" in my_other_set) # false

# eliminar datos de un set
my_other_set.remove("andres")
print(my_other_set)

#limpiar todo el set
my_other_set.clear()
print(len(my_other_set)) # 0 elementos

# eliminar todo el set
del my_other_set
#print(my_other_set) my_other_set is not defined

# uniendo set con metodo union
my_new_set = {"gallo", "caballo", "pollo"}
my_animals = {"pollo", "iguana", "serpiente"}

my_union_set = my_new_set.union(my_animals)
print(my_union_set) # {'caballo', 'pollo', 'gallo', 'serpiente', 'iguana'} 

# viendo la diferencia entre un set y otro
print(my_new_set.difference(my_animals)) #{'caballo', 'gallo'}