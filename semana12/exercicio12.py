#Escreva um programa que cria um array com os números de 1 a 10 e os imprime na ordem inversa.













#Escreva um programa que solicita ao usuário que insira 5 números inteiros e armazene-os em um array. Em seguida, calcule e exiba a soma e a média dos números.

def y(lista):
    for x in range(0,5):
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

#Escreva um programa que cria um array com 5 números inteiros digitados pelo usuário. Em seguida, encontre e exiba o maior e o menor número do array e suas respectivas posições. 

def y(lista,maior,menor):
    for x in range(0,4):
        n = int(input("Digite um número: "))
        lista.append(n)
def u(lista,maior,menor):
    for x in lista:
        if maior < x:
            maior = x
        if menor > x:
            menor = x
            
    print("O maior valor é",maior,"A posição do valor na lista é ",lista.index(maior))
    print("O menor valor é",menor,"A posição do valor na lista é ",lista.index(menor))
def main():
    lista = []
    n = int(input("Digite um número: "))
    lista.append(n)
    maior = n
    menor = n
    y(lista,maior,menor)
    u(lista,maior,menor)
main()
#Escreva um programa que cria dois arrays de tamanho igual, preenchidos com números inteiros digitados pelo usuário. Em seguida, crie um terceiro array que contenha a soma dos elementos correspondentes dos arrays anteriores.




















#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 100. Em seguida, exiba apenas os números pares. Utilize a função rand



























#Escreva um programa que cria um array com 5 valores inteiros digitados pelo usuário. Em seguida, solicite ao usuário que digite um número e verifique se esse número está presente no array.

























#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 50. Em seguida, exiba a quantidade de números pares e a quantidade de números ímpares no array.


















#Escreva um algoritmo que contenha um array e apresente o seguinte menu:

