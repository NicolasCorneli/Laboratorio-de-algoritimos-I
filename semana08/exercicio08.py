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
