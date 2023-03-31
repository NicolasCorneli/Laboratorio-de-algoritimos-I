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
    
    
