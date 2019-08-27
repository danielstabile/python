#adicional 2
#Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, 
#quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! 

entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = entrada // 86400
resto = entrada % 86400
hora = resto // 3600
resto= resto % 3600
minuto = resto // 60
segundo = resto % 60

print(dia, "dias,", hora, "horas,", minuto, "minutos e", segundo, "segundos.")