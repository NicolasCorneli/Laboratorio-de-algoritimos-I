#Faça um algoritmo que contenha duas funções:
#Função 1: exiba um Olá
#Função 2: exiba um Tchau

def ola():
    print("Olá")
def tchau():
    print("Tchau")
def main():
    ola()
    tchau()
main()

#Faça um algoritmo que receba um valor e apresente o dobro e o triplo do valor.

valor = int(input("Digite um valor: "))
def dobroTriplo(valor):
    dobro = valor * 2
    triplo = valor * 3
    print("O dobro é: ",dobro,",O triplo é: ",triplo)
def main():
    dobroTriplo(valor)
main()

#mercado QUIOSQUE

def laranjas():
    qntdLaranjas = int(input("Digite quantas laranjas deseja comprar: "))
    if qntdLaranjas > 12:
        valor = 0.25
        valorFinal = qntdLaranjas * valor
        print(valorFinal)
    else:
        valor = 0.40
        valorFinal = qntdLaranjas * valor
        print(valorFinal)
def main():
    laranjas()
main()


#Faça um algoritmo que leia cinco notas e faça a média das notas, após isso informe a situação do aluno:

nota = 0
media = 0
for x in range(1,6):
    notas = float(input("Digite sua nota: "))
    nota = nota + notas
media = nota / 5
def situacao():
    if media >= 7:
        print("Aprovado!")
    elif media >= 4 and media < 7:
        print("Exame!")
    else:
        print("Reprovado!")
def main():
    situacao()
main()

#Faça um algoritmo que apresente o seguinte menu:

def menu():
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Opção:"))
    return opcao
    
def saque(saldo):
    valorSaque = float(input("Digite um valor que deseja sacar: "))
    saldo = saldo - valorSaque
    if valorSaque > saldo:
        print("Você não pode sacar esse valor")
    return saldo

def depositar(saldo):
    deposito = float(input("Digite o valor que deseja depositar: "))
    saldo = saldo + deposito
    return saldo

def verSaldo(saldo):
    print("Seu saldo é:",saldo)

def main():
    saldo = 0
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            saldo = saque(saldo) 
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            verSaldo(saldo)    
        elif opcao == 4:
            print("Até logo")
        else: 
            print("Digite uma opção válida")
main()

#Faça um programa com uma função chamada somaImposto.

def somaImposto(taxaImposto,custo):
    custo = float(input("Digite o valor do produto: "))
    imposto = custo * 5 / 100
    taxaImposto = imposto + custo
    print("O valor final do produto é:",taxaImposto)
def main():
    taxaImposto = 0
    custo = 0
    somaImposto(taxaImposto,custo)
main()

