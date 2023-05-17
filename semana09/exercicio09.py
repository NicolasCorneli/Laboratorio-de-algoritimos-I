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

#Faça uma função que receba um número como parâmetro e retorne a soma de todos os números naturais menores ou iguais a ele.

def fsoma(x,soma):
    for i in range(0,x+1):
        soma = soma + i
    print(soma)

def main():
    soma = 0
    x = int(input("Digite um número: "))
    fsoma(x,soma)
main()


#Uma Empresa deseja efetuar uma pesquisa de ibope sobre a aceitação de um certo produto lançado por ela no mercado.

def fsimnao(produto,qntdpessoas,sim,nao):
    produto = input("O produto deve estar no mercado ? ").upper()
    if produto == "SIM":
        qntdpessoas = qntdpessoas + 1
        sim = sim + 1
    elif produto == "NÃO":
        qntdpessoas = qntdpessoas + 1
        nao = nao + 1
    else:
        print("Responda com sim ou não")
    return qntdpessoas,sim,nao
def main():
    produto = 0
    qntdpessoas = 0
    sim = 0
    nao = 0
    while qntdpessoas < 20:
        qntdpessoas,sim,nao = fsimnao(produto,qntdpessoas,sim,nao)
    print("A quantidade de pessoas que responderam com SIM é: ",sim)
    print("A quantidade de pessoas que responderam com NÃO é: ",nao)
main()

#Uma empresa de pesquisa deseja saber qual jornal é mais lido em Santa Maria (A, B ou C).

