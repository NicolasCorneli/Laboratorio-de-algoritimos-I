





























#Escreva um programa que solicita ao usuário que insira 5 números inteiros e armazene-os em um array. Em seguida, calcule e exiba a soma e a média dos números.

def y(lista):
    for x in range(1,6):
        n = int(input("Digite um número: "))
        lista.append(n)
def u(lista,media,soma):
    for x in lista:
        soma = soma + x
    media = soma / 5
    print(lista)
    print(media)
    print(soma)
def main():
    soma = 0
    media = 0
    lista = []
    y(lista)
    u(lista,media,soma)
    
main()   
