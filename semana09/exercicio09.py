#Escreva uma função que receba dois números como parâmetros e retorne a soma deles.

def fsoma(x,y):
    soma = x + y
    print(soma)

def main():
    soma = 0
    x = int(input("Digite um número: "))
    y = int(input("Digite um número: "))
    fsoma(x,y)
main()
