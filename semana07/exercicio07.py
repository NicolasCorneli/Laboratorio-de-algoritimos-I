#Faça um programa que exiba na tela os números de 1 a 10 utilizando o laço de repetição for.

for x in range(1,11):
    print(x)
    
#Crie um programa que calcule e exiba na tela a média aritmética de um conjunto de números lidos do usuário utilizando o laço de repetição for.

contador = 0
soma = 0
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
for x in range(primeiro+1,segundo):
    soma = soma + x
    contador = contador + 1
    media = soma / contador
print("A média dos valores entre os números digitados é: ",media)

#Escreva um programa que imprima na tela a sequência de Fibonacci até o décimo termo utilizando o laço de repetição for.

primeiro = 0
segundo = 1
for x in range(3,11):
    proximo = primeiro + segundo
    print(proximo)
    primeiro = segundo
    segundo = proximo
    
#Faça um algoritmo que leia 10 números inteiros e ao final apresente:
#Quantidade de números pares digitados
#Quantidade de números ímpares digitados
#Quantidade de zeros digitados

par = 0
impar = 0
zero = 0
for x in range(1,11):
    n = int(input("Digite um número: "))
    if n %2 ==0:
        par = par + 1
    else:
        impar = impar + 1
    if n == 0:
        zero = zero + 1
print("Quantidade de números pares: ",par)
print("Quantidade de números ímpares: ",impar)
print("Quantidade de zeros: ",zero)

#Foi realizada uma pesquisa de algumas características físicas da população de um certa região. Foram entrevistadas 15 pessoas e coletados os seguintes dados:

meninas = 0
olhosAzuis = 0
olhosCastanhos = 0
olhosVerdes = 0
loiros = 0
castanhos = 0
pretos = 0
m = 0
f = 0
print("A- sexo: M (masculino) e F (feminino)")
print("B- cor dos olhos: A (azuis), V (verdes) e C (castanhos)")
print("C- cor dos cabelos: L (loiros), C (castanhos) e P (pretos)")
print("D- idade")
sexo = input("Digite seu genêro, M ou F: ").upper()
corOlhos = input("Digite a cor de seus olhos, A, V ou C: ").upper()
corCabelo = input("Digite a cor do seu cabelo, L, C ou P: ").upper()
idade = int(input("Digite sua idade: "))
if sexo == "F":
    if corOlhos == "V":
        if corCabelo == "L":
            if idade > 18 and idade < 35:
                meninas = meninas + 1
maior = idade
for x in range(1,15):
    sexo = input("Digite seu genêro, M ou F: ").upper()
    corOlhos = input("Digite a cor de seus olhos, A, V ou C: ").upper()
    corCabelo = input("Digite a cor do seu cabelo, L, C ou P: ").upper()
    idade = int(input("Digite sua idade: "))
    if maior < idade:
        maior = idade
    if sexo == "F":
            if corOlhos == "V":
                if corCabelo == "L":
                    if idade > 18 and idade < 35:
                        meninas = meninas + 1
    if corOlhos == "A":
        olhosAzuis = olhosAzuis + 1
    if corOlhos == "V":
        olhosVerdes = olhosVerdes + 1
    if corOlhos == "C":
        olhosCastanhos = olhosCastanhos + 1
    if corCabelo == "L":
        loiros = loiros + 1
    if corCabelo == "C":
        castanhos = castanhos + 1
    if corCabelo == "P":
        pretos =  pretos + 1
    if sexo == "M":
        m = m + 1
        f = f + 1
olhosAzuisPorcentagem = olhosAzuis / 15
olhosAzuisPorcentagem = olhosAzuisPorcentagem * 100
olhosVerdesPorcentagem = olhosVerdes / 15
olhosVerdesPorcentagem = olhosVerdesPorcentagem * 100
olhosCastanhosPorcentagem = olhosCastanhos / 15
olhosCastanhosPorcentagem = olhosCastanhosPorcentagem * 100
cabeloLoiroPorcentagem = loiros / 15
cabeloLoiroPorcentagem = cabeloLoiroPorcentagem * 100
cabeloCastanhoPorcentagem = castanhos / 15
cabeloCastanhoPorcentagem = cabeloCastanhoPorcentagem * 100
cabeloPretoPorcentagem = pretos / 15
cabeloPretoPorcentagem = cabeloPretoPorcentagem * 100
porcentagemF = f / 15
porcentagemF = porcentagemF * 100
porcentagemM = m / 15
porcentagemM = porcentagemM * 100
print("A maior idade do grupo é: ",maior)
print("A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos loiros é: ",meninas)
print("A porcentagem de pessoas com os olhos azuis: ",olhosAzuisPorcentagem)
print("A porcentagem de pessoas com os olhos verdes: ",olhosVerdesPorcentagem)
print("A porcentagem de pessoas com os olhos castanhos: ",olhosCastanhosPorcentagem)
print("A porcentagem de cabelos loiros é: ",cabeloLoiroPorcentagem)
print("A porcentagem de cabelos castanhos é: ",cabeloCastanhoPorcentagem)
print("A porcentagem de cabelos pretos é: ",cabeloPretoPorcentagem)
print("A porcentagem de pessoas do sexo masculino é: ",porcentagemM)
print("A porcentagem de pessoas do sexo feminino é: ",porcentagemM)

#Fazer um programa para encontrar todos os números pares entre 1 e 100.

