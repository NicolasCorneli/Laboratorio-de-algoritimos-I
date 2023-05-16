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

#Escreva uma função que verifique se um número é primo. A função deve receber um número como parâmetro e retornar True se ele for primo, caso contrário, retorna False.

def fprimo(x):
    if x == 2:
        print("é primo")
    for i in range(2,x):
        if x %i == 0:
            print("Não é primo")
            break
        else:
            print("é primo")
            break

def main():
    x = int(input("Digite um número: "))
    fprimo(x)
main()

#Faça uma função que receba um número como parâmetro e retorne o seu dobro.

def fdobro(x):
    dobro = x * 2
    print(dobro)

def main():
    dobro = 0
    x = int(input("Digite um número: "))
    fdobro(x)
main()

#Escreva uma função que receba uma temperatura em graus Celsius como parâmetro e retorne a temperatura equivalente em graus Fahrenheit.

def fcelsius(x):
    f = (x*9/5) + 32
    print(f)

def main():
    f = 0
    x = int(input("Digite a temperatura em graus celsius: "))
    fcelsius(x)
main()
