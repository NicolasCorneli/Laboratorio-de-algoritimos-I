#Faça um algoritmo que leia dois valores e apresente:
#O maior deles
#O menor deles

#Obs. o algoritmo deve verificar se os valores digitados são iguais

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 > n2:
    print("O maior valor é:", n1)
    print("O menor valor é:", n2)
elif n2 > n1:
    print("O maior valor é:", n2)
    print("O menor valor é:", n1)
else:
    print("Os valores são iguais")
    
    #Um sistema de uma loja de roupas permite que as peças de roupas sejam vendidas de três formas diferentes: 
#À vista.
#2 vezes.
#3 vezes.
#Para isso, o sistema deve ler o valor da peça, a opção de pagamento e apresentar o valor das parcelas.

precoRoupa = float(input("Digite o valor do produto: "))

print("1 - À vista")
print("2 - Parcelar em 2 vezes")
print("3 - Parcelar em 3 vezes")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("O valor da roupa à vista é: ", precoRoupa)
elif opcao == 2:
    valorParcela = precoRoupa / 2
    print("O valor da roupa é: ", precoRoupa)
    print("O valor parcelado em 2 vezes é: ", valorParcela)
elif opcao == 3:
    valorParcela = precoRoupa / 3
    print("O valor da roupa é: ", precoRoupa)
    print("O valor parcelado em 3 vezes é: ", valorParcela)
else:
    print("Digite uma opção válida")
    
    
#Um professor quer fazer um algoritmo para testar se uma questão de múltipla escolha está certa. Para isso, leia a questão assinalada pelo aluno e verifique:
#A - resposta errada
#B - resposta certa
#C - resposta errada
#D - resposta errada

resposta = input("Escolha a resposta: ").upper()

if resposta == "A":
    print("Resposta errada")
elif resposta == "B":
    print("Resposta certa")
elif resposta == "C":
    print("Resposta errada")
elif resposta == "D":
    print("Resposta errada")
else:
    print("Digite uma resposta válida")
    
    
#Faça um algoritmo que leia dois valores. Posteriormente leia uma opção do menu:  
#Somar os dois valores.
#Subtrair os dois valores.
#Multiplicar os dois valores.
#Dividir os dois valores

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

print("1 - Somar os 2 valores")
print("2 - Subtrair os 2 valores")
print("3 - Multiplicar os 2 valores")
print("4 - Dividir os 2 valores")

opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    resposta = n1 + n2
    print("A resposta é: ", resposta)
elif opcao == 2:
    resposta = n1 - n2
    print("A resposta é: ", resposta)
elif opcao == 3:
    resposta = n1 * n2
    print("A resposta é: ", resposta)
elif opcao == 4:
    resposta = n1 / n2
    print("A resposta é: ", resposta)
else:
    print("Digite uma opção válida")

    
    
