# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

#1° Ejercicio

print("Ingrese un número")
numero_1 = int(input())

print("Ingrese otro número")
numero_2 = int(input())

diferencia = numero_1 - numero_2

if numero_1 > numero_2:
    print("El resultado de la resta entre", numero_1, "y", numero_2, "es positiva y es igual a", diferencia)
elif numero_1 < numero_2:
    print("El resultado de la resta entre", numero_1, "y", numero_2, "es negativa y es igual a", diferencia)
else:
    print("El resultado de la resta entre", numero_1, "y", numero_2, "es igual a", diferencia)


"""
Otra opción para ahorrar líneas sería:

numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: "))
"""

