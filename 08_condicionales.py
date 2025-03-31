### Condicionales ###

# nos permite definir el flujo de nuestro codigo en base a condiciones booleanas

my_condition = True

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 3

if my_condition > 10 and my_condition < 20:
    print("es verdadera la respuesta por que el numero es mayor a 10 y menor que 20")
elif my_condition > 20:
    print()
else:  
    print("es falsa la respuesta por que el numero es menor o igual a 10")


print("La ejecución continua")