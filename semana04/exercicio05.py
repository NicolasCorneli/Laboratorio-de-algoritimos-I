#Crie um programa que leia o nome, o salário e o tempo de serviço de um funcionário e informe se ele tem direito a receber um aumento. O funcionário deve ter pelo menos 5 anos de serviço e o salário não pode ser superior a R$ 2.000,00 para receber o aumento de 10%. Caso contrário, o aumento é de 5%.


nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
tempoServico = int(input("Digite seu tempo de serviço em anos(se o seu tempo de serviço for inferior a 1 ano, digite o numero 1): "))
if tempoServico >= 5 and salario <= 2000:
    salarioNovo = salario * 1.10
    print(nome,"você recebeu um aumento de 10%, seu salário foi de: ", salarioNovo)
else:
    salarioNovo = salario * 1.05
    print(nome, "você recebeu um aumento de 5%, seu salário foi de: ", salarioNovo)
    
    
#Faça um script que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


base = float(input("Digite o valor da base do triângulo: "))
cateto1 = float(input("Digite o valor de um cateto do triângulo: "))
cateto2 = float(input("Digite o valor do outro cateto do triângulo: "))

if base == cateto1 and cateto1 == cateto2:
    print("O triângulo é equilátero")
elif base == cateto1 or base == cateto2 or cateto1 == cateto2:
    print("O triângulo é isósceles")
elif base != cateto1 and base != cateto2 and cateto2 != cateto1:
    print("O triângulo é escaleno")
    
    
#Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Também solicite qual a % de frequência e aula, verifique e apresente a seguinte mensagem:

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua outra nota: "))
media = (n1 + n2) / 2
frequencia = int(input("Digite sua frequência (%): "))
if media >= 7 and frequencia >= 75:
    print("Você está aprovado")
elif media >= 4 and media < 7 and frequencia >= 75:
    print("Você está em exame")
else:
    print("Você está reprovado")
    
    
#Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:


n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
media = (n1 + n2) / 2

if media >= 9 and media <= 10:
    print("Conceito A, suas notas foram ",n1,"e",n2,"sua média foi: ",media,"Você foi aprovado")
elif media >= 7.5 and media < 9:
    print("Conceito B, suas notas foram ",n1,"e",n2,"sua média foi: ",media,"Você foi aprovado")
elif media >= 6 and media < 7.5:
    print("Conceito C, suas notas foram ",n1,"e",n2,"sua média foi: ",media,"Você foi aprovado")
elif media >= 4 and media < 6:
    print("Conceito D, suas notas foram ",n1,"e",n2,"sua média foi: ",media,"Você foi reprovado")
elif media >= 0 and media < 4:
    print("Conceito E, suas notas foram ",n1,"e",n2,"sua média foi: ",media,"Você foi reprovado")

#Faça um script que faça 5 perguntas para uma pessoa sobre um crime.


