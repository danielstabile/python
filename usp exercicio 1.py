#Exercício 1
#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
#calcule e imprima (saída de dados) seu perímetro e sua área. Observação: a saída deve estar no formato: "perímetro: x - área: y"

entrada = int(input("Digite o valor correspondente ao lado de um quadrado: "))
perimetro = entrada * 4
area = entrada * entrada

print("perímetro:", perimetro, "- área:", area)