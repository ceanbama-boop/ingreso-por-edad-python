# Paso 1 : Solicitar al usuarrio que ingrese la edad del cliente

from operator import truediv


edad = int(input("Ingrese la edad del cliente: "))


# Paso 2 : Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca

permitido = True if  edad > 18 or edad < 60 else  False      # este metodo o tecnica se llama ternario
    
# Paso 3 : Mostrar al usuario si el cliente puede o no ingresar a la discoteca

if permitido:
    print("Puedes ingresar a la discoteca")
else:
    print("Lo sentimos no puedes ingresar a la discoteca siendo menor a 18")
