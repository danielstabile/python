#exercicio 1: Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 

idade = input("Digite sua idade: ")

if int(idade) >= 18:
	msg = "Você é maior de idade"
else:
    msg = "Você é menor de idade"

print(msg)

