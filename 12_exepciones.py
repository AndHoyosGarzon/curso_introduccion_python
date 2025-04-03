### Exepciones o manejo de errores  ###
number_one = 1
number_two = 2

# Reasigancion creando error
number_two = "1"

try: # cuando todo sale bien el try maneja el proceso
    print(number_one + number_two)
    print("No se ha producido error")
except: # el programa no revienta ya que estamos manejando los errores
    print("Se ha producido un error")
else: # se pone opcionalmente, se ejecuta siempre y cuando el porgrama se ejecute correctamente
    print("La ejecucion continua correctamente")
finally:# opcional: se ejecuta siempre ya que muestra el final del proceso
    print("La ejecucion continua")


### Captura de exepciones por tipo ###
number_Three = 3
number_four = 4

number_Three = "3"

try:
    print("Todo ha salido bien la suma es", number_Three + number_four)
except ValueError as error:
    print("El error es de tipo", error)
except Exception as exception_error:
    print("Exepcion generica si o si se cumple cuando no se capturan otros errores", exception_error)

    