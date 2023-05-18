def y(valores):
    for x in range (1,11):
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
