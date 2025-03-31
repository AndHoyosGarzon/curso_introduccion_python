### STRINGS ###
my_string = "Mi string"
my_other_string = "Otro string"

print(len(my_string)) # 9 caracteres
print(len(my_other_string)) # 11 caracteres

my_new_line_string = "Este es un nuevo string largo con un salto de linea \n por medio de una expression regular"
print(my_new_line_string)

my_tab_string = "Este es un string con \t tabulacion larga ..."
print(my_tab_string)

my_scape_string = "\tEste es un string con escape de \ncomillas literales"
print(my_scape_string)


### Formateo ###
name, surname, age = "andres", "Felipe", 33
print("Mi nombre es {} {} y mi edad es {} ".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d "%(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


### Desempaquetado de caracteres ###
language = "Python"

a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


### Division de strings ###
lenguage_programation = "Python 3"

lengueage_slice = lenguage_programation[1:3]

print(lengueage_slice) #inicia en el indice 0 contando y termina en la longitud 3, osea imprime yt


### Reverse ###
lenguage_programation_2 = "Python"

lengueage_slice_2 = lenguage_programation_2[::-1]
print(lengueage_slice_2) # nohtyP


### Funciones del sistema para lso tipos de datos Strings ###
new_language = ("javaScript")
print(new_language.capitalize()) # primera letra en mayuscula
print(new_language.upper()) # me transforma todo el string en mayuscula
print(new_language.lower()) # me transforma todo el string en minuscula
print(new_language.count("t")) # cuanta cuantas letras "t" tiene el string 
print(new_language.endswith("p")) # nos dice si termina con la letra p en especifico
print(new_language.isnumeric()) # nos arroja un booleano verificando el tipo de dato


































































