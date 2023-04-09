#Uma empresa de pesquisa deseja saber a média de altura e idade das pessoas, para isso, crie um algoritmo que apresente o seguinte menu:

qntdPessoas = 0
alturaPessoas = 0
idadePessoas = 0
opcao = 0
while opcao != 3:
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar média parcial de altura e idade")
    print("3 - Sair e mostrar a média final de altura e idade")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        idade = int(input("Digite sua idade: "))
        idadePessoas = idadePessoas + idade
        altura = float(input("Digite sua altura: "))
        alturaPessoas = alturaPessoas + altura
        qntdPessoas = qntdPessoas + 1
    elif opcao == 2:
        mediaParcialIdade = idadePessoas / qntdPessoas
        mediaParcialAltura = alturaPessoas / qntdPessoas
        print("A média parcial de idades é de: ",mediaParcialIdade)
        print("A média parcial de alturas é de: ",mediaParcialAltura)
    elif opcao == 3:
        mediaI = idadePessoas / qntdPessoas
        mediaA = alturaPessoas / qntdPessoas
        print("A média oficial de idades é de: ", mediaI)
        print("A média oficial de alturas é de: ",mediaA)
    else:    
        print("Digite uma opção válida")


#Faça um algoritmo que simule uma conta bancária:

saldoAtual = float(input("Digite o seu saldo atual: "))
opcao = 0
while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Verificar Saldo")
    print("4 - Sair")
    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        saque = float(input("Digite o valor que deseja retirar: "))
        saldoNovo = saldoAtual - saque
        if saldoAtual < saque:
            print("Você não tem fundos suficientes para retirar esse valor")
    elif opcao == 2:
        deposito = float(input("Digite o valor que deseja depositar: "))
        saldoNovo = saldoNovo + deposito
    elif opcao == 3:
        print("O seu saldo atual é de: ",saldoNovo)
    elif opcao == 4:
        print("Até a próxima!")
    else:
        print("Digite uma opção válida")

        
#Fazer um algoritmo que leia diversos números e mostre quantas vezes o número 10 foi digitado. O laço de repetição deve parar quando o usuário digitar 0. 


qntdDigitada = 0
numero = 1
while numero != 0:
    numero = float(input("Digite um número: "))
    if numero == 10:
        qntdDigitada = qntdDigitada + 1
    elif numero == 0:
        print("A quantidade de vezes que o número 10 foi digitada é de: ",qntdDigitada)

        
#Faça um programa que receba a idade e o peso de 7 pessoas, calcule e mostre:


qntdEntradas = 0
somaIdade = 0
somaPeso = 0
maiorIdade = 0
porcentagemIdade = 0
print("Digite a idade e o peso das 7 pessoas")
while qntdEntradas < 7:
    idade = int(input("Digite sua idade: "))
    somaIdade = somaIdade + idade
    if idade >= 18:
        maiorIdade = maiorIdade + 1
    if idade > 10 and idade < 30:
        porcentagemIdade = porcentagemIdade + 1
    peso = float(input("Digite seu peso: "))
    somaPeso = somaPeso + peso
    qntdEntradas = qntdEntradas + 1
    print("-------------")
if porcentagemIdade == 7:
    print("100% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 6:
    print("85.7% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 5:
    print("71.4% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 4:
    print("57.1% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 3:
    print("42.8% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 2:
    print("28.5% das pessoas estão entre 10 e 30 anos")
elif porcentagemIdade == 1:
    print("14.2% das pessoas estão entre 10 e 30 anos")
else:
    print("0% das pessoas estão entre 10 e 30 anos")
mediaIdade = somaIdade / 7
print("A média das idades é: ",mediaIdade)
print("A quantidade de pessoas maiores de idade é: ",maiorIdade)


#Foi feita uma pesquisa entre os 10 habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que informe: 


somaSalario = 0
qntdPessoas = 0
qntdMulheresSalario = 0
while qntdPessoas < 10:
    genero = input("Digite seu gênero: ").upper()
    qntdPessoas = qntdPessoas + 1
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    somaSalario = somaSalario + salario
    if salario <= 100 and genero == "FEMININO":
        qntdMulheresSalario = qntdMulheresSalario + 1
    print("--------------------------------")
media = somaSalario / 10
print("A média dos salários é: ",media)
print("A quantidade de muheres com salário até R$100,00 é: ",qntdMulheresSalario)



#Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.


qntdPessoas = 0
qntdPessoasIdade = 0
while qntdPessoas < 10:
    qntdPessoas = qntdPessoas + 1
    idade = int(input("Digite sua idade: "))
    print("-----------------------")
    if idade >= 18:
        qntdPessoasIdade = qntdPessoasIdade + 1
print("A quantidade de pessoas com idade maior ou igual a 18 é: ",qntdPessoasIdade)



#Faça um programa que receba dez números e usando laços de repetição calcule e mostre a quantidade de números entre 30 e 90. 


qntdNumeros = 0
while qntdNumeros < 10:
    numeros = float(input("Digite um número: "))
    if numeros > 30 and numeros < 90:
        qntdNumeros = qntdNumeros + 1
print("A quantidade de números maiores que 30 e menores que 90 é: ",qntdNumeros)



#Em um prédio com 10 moradores há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores, desenvolva um programa em que cada morador informa qual o elevador que utiliza com mais frequência (A, B ou C). 
#O algoritmo deve contabilizar o total de pessoas que usa cada um dos elevadores e mostrar estes totais e suas respectivas porcentagens no final.


qntdPessoas = 0
elevadorA = 0
elevadorB = 0
elevadorC = 0
while qntdPessoas < 10:
    qntdPessoas = qntdPessoas + 1
    print("1 - A")
    print("2 - B")
    print("3 - C")
    elevador = int(input("Digite qual o elevador que utiliza com mais frequência: "))
    if elevador == 1:
        elevadorA = elevadorA + 1
    elif elevador == 2:
        elevadorB = elevadorB + 1
    elif elevador == 3:
        elevadorC = elevadorC + 1
    else:
        print("Digite um número válido")
    print("-----------------------")
aPorcentagem = elevadorA / 10
aPorcentagem = aPorcentagem * 100
bPorcentagem = elevadorB / 10
bPorcentagem = bPorcentagem * 100
cPorcentagem = elevadorC / 10
cPorcentagem = cPorcentagem * 100
print("A quantidade de pessoas que usam o elevador A é: ",elevadorA,",",aPorcentagem,"%" )
print("A quantidade de pessoas que usam o elevador B é: ",elevadorB,",",bPorcentagem,"%")
print("A quantidade de pessoas que usam o elevador C é: ",elevadorC,",",cPorcentagem,"%")
