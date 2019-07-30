#exercicio 2: Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media >= 6:
	msg = "APROVADO"
else:
	msg = "REPROVADO"

print(msg + ". Média: " + str(media))