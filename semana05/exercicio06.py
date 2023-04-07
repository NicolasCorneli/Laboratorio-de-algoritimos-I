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
