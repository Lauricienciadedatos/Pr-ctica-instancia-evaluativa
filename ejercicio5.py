def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

# Solicitar los valores al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Llamar al función
resultado_suma, resultado_resta = suma_y_resta(num1, num2)

print("El resultado de la suma es:", resultado_suma)
print("El resultado de la resta es:", resultado_resta)