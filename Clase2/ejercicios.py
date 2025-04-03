'''
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par o si
ambos lo son
'''
#Creacion de programa
# Pedir dos números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificar si son pares o impares
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares.")
elif num1 % 2 == 0:
    print(f"El número {num1} es par y {num2} es impar.")
elif num2 % 2 == 0:
    print(f"El número {num2} es par y {num1} es impar.")
else:
    print("Ambos números son impares.")
