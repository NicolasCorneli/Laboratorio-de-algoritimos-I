#Faça um algoritmo que leia 10 valores distintos. Ao final apresente quantos valores são maiores que 100.

def y(valores):
    for x in range (0,10):
        valor = int(input("Digite um valor: "))
        valores.append(valor)
def z(valores,qntdMaiores):
    for x in valores:
        if x > 100:
            qntdMaiores = qntdMaiores + 1
    print(qntdMaiores)
def main():
    qntdMaiores = 0
    valores = []
    y(valores)
    z(valores,qntdMaiores)
    
main()


#Faça um algoritmo que leia tenha um vetor e apresente o seguinte menu:
def menu():
    print("1- Acrescentar número a lista")
    print("2- Retirar número da lista")
    print("3- Ver lista")
    print("4- Sair")
    opc = int(input("Escolha uma opção: "))
    return opc
def acrescentar(numeros):
    numero = int(input("Digite um número para acrescentar a lista: "))
    numeros.append(numero)
    
def retirar(numeros):
    numero = int(input("Digite um número para retirar da lista: "))
    numeros.remove(numero)
    
def lista(numeros):
    print(numeros)


def main():
    opc = 0
    numeros = []
    while opc != 4:
        opc = menu()
        if opc == 1:
            acrescentar(numeros)
        elif opc == 2:
            retirar(numeros)
        elif opc == 3:
            lista(numeros)
main()

