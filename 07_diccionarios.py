### Diccionarios ###

my_dict = dict() # constructor de diccionario
my_other_dict = {}
print(type(my_dict)) # <class 'dict'>

my_other_dict = {
    "Nombre": "andres",
    "apellido": "Hoyos",
    "edad": 33,
    1: "python",
}

print(my_other_dict) #{'Nombre': 'andres', 'apellido': 'Hoyos', 'edad': 33, 1: 'python'}
print(my_other_dict["Nombre"]) # accediendo al valor del la clave nombre = andres
print(my_other_dict[1]) # nos muestra el dato python

# agregando propiedades a un diccionario
my_other_dict["direccion"] = "terranova"
print(my_other_dict) #{'Nombre': 'andres', 'apellido': 'Hoyos', 'edad': 33, 1: 'python', 'direccion': 'terranova'}


### comprobando si tenemos un tipo de clave especifico ###
print("Nombre" in my_other_dict)


### eliminado datos de un diccionario ###
my_other_dict.popitem() #  nos elimina el ultimo dato del diccionario
#print(my_other_dict)

my_other_dict.pop("Nombre") # nos elimina el la clave y el valor ingresado por parametro
#print(my_other_dict) 

del my_other_dict["apellido"] # nos elimina el la clave y el valor ingresado por parametro
#print(my_other_dict)

# my_other_dict.clear() # nos limpia todo el diccionario
#print(my_other_dict) 


### Metodos nativos de los diccionarios ###
my_nuevo_dict = {"papa": "israel", "mama": "tatiana", "hijo": "andres", "nuera": "tatiana"}

print(my_nuevo_dict.items()) # dict_items([('papa', 'israel'), ('mama', 'tatiana'), ('hijo', 'andres'), ('nuera', 'tatiana')])
print(my_nuevo_dict.keys()) # dict_keys(['papa', 'mama', 'hijo', 'nuera'])
print(my_nuevo_dict.values()) # dict_values(['israel', 'tatiana', 'andres', 'tatiana'])

my_copy_dict = dict.fromkeys(my_nuevo_dict) # nos crea un nuevo diccionario donde extrae las claves del diccionario anterior
print(my_copy_dict)
