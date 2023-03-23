#Exemplo.

totalHoras = float(input("Digite o total de horas trabalhadas no mês: "))
salario = totalHoras * 35
if salario < 1000.00:
    n2 = salario + 300.00
    print("já que seu salário normal: R$", salario, "foi inferior a R$1000, demos um bonûs de R$300")
    print("seu salário final é de: R$", n2)
else:
    print("seu salário esse mês é de: R$", salario)
