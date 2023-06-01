#Escreva um programa que cria um array com os números de 1 a 10 e os imprime na ordem inversa.

def y(lista):
    for x in range(0,10):
        lista.append(x)
    print(lista)
def reverso(lista):
    for x in lista:
        rev = lista[::-1]
    print(rev)

def main():
    lista = []
    y(lista)
    reverso(lista)
main()

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

def y(lista1):
    for x in range(0,5):
        n = int(input("Digite um número para botar na primeira lista: "))
        lista1.append(n)
def u(lista2):
    for x in range(0,5):
        n = int(input("Digite um número para botar na segunda lista: "))
        lista2.append(n)
def g(lista1,lista2,lista3):
    a = lista1[0] + lista2[0]
    lista3.append(a)
    b = lista1[1] + lista2[1]
    lista3.append(b)
    c = lista1[2] + lista2[2]
    lista3.append(c)
    d = lista1[3] + lista2[3]
    lista3.append(d)
    e = lista1[4] + lista2[4]
    lista3.append(e)
    print(lista3)
def main():
    lista1 = []
    lista2 = []
    lista3 = []
    y(lista1)
    u(lista2)
    g(lista1,lista2,lista3)
main()

#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 100. Em seguida, exiba apenas os números pares. Utilize a função rand

def y(lista):
    for x in range(0,10):
        n = int(input("Digite algum número entre 1 e 100: "))
        if n <= 1 or n >= 100:
            print("Digite um número entre 1 e 100")
        elif n %2 == 0:
            lista.append(n)
    print("Os números pares entre 1 e 100 digitados são:",lista)

def main():
    lista = []
    y(lista)
main()

#Escreva um programa que cria um array com 5 valores inteiros digitados pelo usuário. Em seguida, solicite ao usuário que digite um número e verifique se esse número está presente no array.

def y(lista):
    for x in range(0,5):
        n = int(input("Digite um número: "))
        lista.append(n)
def u(lista):
    zz = int(input("Verificar se o número está presente na lista: "))
    if zz in lista:
        print("O número está presente na lista")
    else:
        print("O número não está presente na lista")

def main():
    lista = []
    y(lista)
    u(lista)
main()

#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 50. Em seguida, exiba a quantidade de números pares e a quantidade de números ímpares no array.

def y(lista,pares,impares):
    for x in range(0,10):
        n = int(input("Digite algum número entre 1 e 50: "))
        if n <= 1 or n >= 50:
            print("Digite um número entre 1 e 50")
        else:
            lista.append(n)
            if n %2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
    print("A quantidade de números pares na lista é: ",pares)
    print("A quantidade de números ímpares na lista é: ",impares)

def main():
    pares = 0
    impares = 0
    lista = []
    y(lista,pares,impares)
main()

#Escreva um algoritmo que contenha um array e apresente o seguinte menu:

def menu():
    print("1- Inserir item")
    print("2- Listar itens")
    print("3- Retirar item")
    print("4- Retirar todos os itens")
    print("5- Sair")
    opc = int(input("Digite uma opção: "))
    return opc
    
def inserir(lista):
        n = int(input("Digite números pares para inserir na lista: "))
        if n %2 == 0:
            lista.append(n)
        else:
            print("ERRO! Digite somente números pares!")
            n = menu()
def retirar(lista):
    n = int(input("Digite um número para retirar da lista: "))
    lista.remove(n)

def retirarTodos(lista):
    del lista[:]

def main():
    opc = 0
    lista = []
    while opc != 5:
        opc = menu()
        if opc == 1:
            inserir(lista)
        elif opc == 2:
            print(lista)
        elif opc == 3:
            retirar(lista)
        elif opc == 4:
            retirarTodos(lista)
        elif opc == 5:
            print("Goodbye!")
        else:
            print("Digite uma opção válida")
main()
