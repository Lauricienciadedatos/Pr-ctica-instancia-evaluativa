def comparar_numeros(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if comparar_numeros(numero1, numero2):
    print("TRUE")
