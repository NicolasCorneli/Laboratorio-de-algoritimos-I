#Fazer um programa em python que pergunta um valor em metros e imprime o correspondente em decímetros, centímetros e milímetros.

def valores(metro):
    decimetro = metro * 10
    centimetro = metro * 100
    milimetro = metro * 1000
    return decimetro,centimetro,milimetro
def verValores(decimetro,centimetro,milimetro):
    print("O valor em decimetros é: ",decimetro)
    print("O valor em centimetros é: ",centimetro)
    print("O valor em milimetros é: ",milimetro)
def main():
    decimetro = 0
    centimetro = 0
    milimetro = 0
    metro = float(input("Digite um valor em metros: "))
    decimetro,centimetro,milimetro = valores(metro)
    verValores(decimetro,centimetro,milimetro)
main()

#Faça um programa que receba a idade e o peso de 7 pessoas, calcule e mostre:

def idadepeso(mediaIdade,mediaPeso,qntdpessoas,idade,peso):
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))
    mediaIdade = mediaIdade + idade
    mediaPeso = mediaPeso + peso
    qntdpessoas = qntdpessoas + 1
    return qntdpessoas,mediaIdade,mediaPeso,idade,peso

def media(mediaIdade,mediaPeso):
    mediaIdadeCalculada = mediaIdade / 7
    mediaPesoCalculada = mediaPeso / 7
    print("Média idade:", mediaIdadeCalculada)
    print("Média peso:", mediaPesoCalculada)
    return mediaIdadeCalculada, mediaPesoCalculada

def maiorIdade(idade,qntdMaior):
    if idade >= 18:
        qntdMaior = qntdMaior + 1
    print("Quantidade de maiores de idade:",qntdMaior)
    return qntdMaior

def porcentagem(idade,porcentagemIdades):
    if idade > 10 and idade < 30:
        porcentagemIdades = porcentagemIdades + 1
    return porcentagemIdades
def por(porcentagemIdades,qntdpessoas):
    porcentagemIdades = porcentagemIdades / qntdpessoas * 100
    print("Porcentagem das idades entre 10 e 30:",porcentagemIdades)
    return porcentagemIdades

def main():
    qntdpessoas = 0
    peso = 0
    idade = 0
    mediaPeso = 0
    mediaIdade = 0
    qntdMaior = 0
    porcentagemIdades = 0
    while qntdpessoas < 7:
        qntdpessoas,mediaIdade,mediaPeso,idade,peso = idadepeso(mediaIdade, mediaPeso, qntdpessoas, idade, peso)
        qntdMaior = maiorIdade(idade,qntdMaior)
        porcentagemIdades = porcentagem(idade,porcentagemIdades)
    porcentagemIdades = por(porcentagemIdades,qntdpessoas)
    mediaIdade,mediaPeso = media(mediaIdade,mediaPeso)

main()
