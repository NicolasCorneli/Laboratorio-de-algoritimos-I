#Exemplo.

totalHoras = float(input("Digite o total de horas trabalhadas no mês: "))
salario = totalHoras * 35
if salario < 1000.00:
    n2 = salario + 300.00
    print("já que seu salário normal: R$", salario, "foi inferior a R$1000, demos um bonûs de R$300")
    print("seu salário final é de: R$", n2)
else:
    print("seu salário esse mês é de: R$", salario)
    
#Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.   
    
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
if n1 > n2:
    print("A ordem crescente é: ", n2, n1)
else:
    print("A ordem crescente é: ", n1, n2)    
 
#Faça um algoritmo que leia o ano de nascimento de uma pessoa e verifique se ela pode ou não votar (desconsidere o mês de nascimento).

anoNascimento = int(input("Digite seu ano de nascimento: "))
z1 = 2023 - anoNascimento
if z1 >= 18:
    print("Você pode votar")
else:
    print("Você não pode votar")
    
#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.    
    
    valorBotar = float(input("Digite o valor que deseja botar: "))
precoGasolina = 5.54
qntdLitros = valorBotar / precoGasolina

print("A quantidade de litros de gasolina que vai ser adicionada é: ", qntdLitros)
    
#Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação:
#maior de idade;
#menor de idade;
    
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")    
    
    
#Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.


n1 = float(input("Digite um número: "))
dobro = n1 * 2
if n1 >= 0:
    print("O dobro do número digitado é: ", dobro)
else:
    print("Número inválido")
    
    
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
