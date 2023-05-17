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

def abc(a,b,c,fjornal):
    jornal = input("Qual jornal você lê ?, A, B ou C: ").upper()
    if jornal == "A":
        a = a + 1
        fjornal = fjornal + 1
    elif jornal == "B":
        b = b + 1
        fjornal = fjornal + 1
    elif jornal == "C":
        c = c + 1
        jornal = fjornal + 1
    else:
        print("Digite uma opção válida")
    return fjornal,a,b,c

def porcentagem(a,b,c,porcentagemA,porcentagemB,porcentagemC):
    porcentagemA = a / 20
    porcentagemA = porcentagemA * 100
    porcentagemB = b / 20
    porcentagemB = porcentagemB * 100
    porcentagemC = c / 20
    porcentagemC = porcentagemC * 100
    return porcentagemA,porcentagemB,porcentagemC

def fcrescente(a,b,c,porcentagemA,porcentagemB,porcentagemC):
    if a < b and b < c:
        print(porcentagemA,porcentagemB,porcentagemC,",O jornal mais lido é o C, depois o B e por último o A")
    elif b < c and c < a:
        print(porcentagemB,porcentagemC,porcentagemA,",O jornal mais lido é o A, depois o C e por último o B")
    elif c < a and a < b:
        print(porcentagemC,porcentagemA,porcentagemB,",O jornal mais lido é o B, depois o A e por último o C")
    elif a < c and c < b:
        print(porcentagemA,porcentagemC,porcentagemB,",O jornal mais lido é o B, depois o C e por último o A")
    elif b < a and a < c:
        print(porcentagemB,porcentagemA,porcentagemC,",O jornal mais lido é o C, depois o A e por último o B")
    elif c < b and b < a:
        print(porcentagemC,porcentagemB,porcentagemA,",O jornal mais lido é o A, depois o B e por último o C")
    return a,b,c,porcentagemA,porcentagemB,porcentagemC
def main():
    a = 0
    b = 0
    c = 0
    fjornal = 0
    porcentagemA = 0
    porcentagemB = 0
    porcentagemC = 0
    while fjornal < 20:
        fjornal,a,b,c = abc(a,b,c,fjornal)
    porcentagemA,porcentagemB,porcentagemC = porcentagem(a,b,c,porcentagemA,porcentagemB,porcentagemC)
    a,b,c,porcentagemA,porcentagemB,porcentagemC = fcrescente(a,b,c,porcentagemA,porcentagemB,porcentagemC)
main()
