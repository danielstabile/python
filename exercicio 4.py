#4 Escreva um programa que ordene uma lista numérica com três elementos.

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

numero_ordenado = n1, n2, n3
numero_ordenado = sorted(numero_ordenado)

print("Numeros ordenados: " + str(numero_ordenado))