#A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el 
#programa la ejecución del mismo con al menos otros dos nombres más, 
#es decir, tres mensajes con tres nombres distintos. 
#Recuerda: en estos ejercicios trabajamos argumentos. ###

def saludar(nombre):
    mensaje = "Hola " + nombre + ", ¿Qué tal?"
    print(mensaje)

nombres = ["Ana", "Laura", "Luis"]

for nombre in nombres:
    saludar(nombre)