#Exemplo.

totalHoras = float(input("Digite o total de horas trabalhadas no mês: "))
salario = totalHoras * 35
if salario < 1000.00:
    n2 = salario + 300.00
    print("já que seu salário normal: R$", salario, "foi inferior a R$1000, demos um bonûs de R$300")
    print("seu salário final é de: R$", n2)
else:
    print("seu salário esse mês é de: R$", salario)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde ´ h corresponde a altura): 
#Homens: (72.7 ∗ h) − 58
#Mulheres: (62, 1 ∗ h) − 44, 7
    
    h = float(input("Digite sua altura: "))
generoMasculino = (72.7 * h) - 58
generoFeminino = (62.1 * h) - 44.7
genero = input("Digite seu gênero: ")
if genero == "Masculino":
    print("Seu peso ideal é de: ", generoMasculino)
if genero == "Feminino":
    print("Seu peso ideal é de: ", generoFeminino)
else:
    print("valor inválido")
