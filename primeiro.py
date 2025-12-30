# print("Esse é meu primeiro script em Python")

def moeda(valor):
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")
def ler_valor (msg):
    valor = input(msg)
    valor = valor.replace(",", ".")
    return float(valor)

while True:
    salario = ler_valor("Digite seu Salario:")
    aluguel = ler_valor("Digite o valor do Aluguel: ")
    energia = ler_valor("Digite o valor da Energia:")
    agua = ler_valor("Digite o valor da Água:")
    internet = ler_valor("Digite o valor da sua Internet:")
    cartao = ler_valor("Digite o valor do Cartão:")
    assinaturas = ler_valor("Digite o valor das Assinaturas:")

    restante = salario - aluguel - energia - agua - internet - cartao - assinaturas

    print("\nResumo:")
    print("Salario: R$", salario)
    print("Aluguel: R$", aluguel)
    print("Energia: R$", energia)
    print("Água: R$", agua)
    print("Internet: R$", internet)
    print("Cartão R$", cartao)
    print("Assinaturas R$", assinaturas)

    if restante > 0:
        print("\nSaldo restante: R$", moeda(restante))
        print("Boa! Sobrou dinheiro:")
    elif restante == 0:
        print("Saldo igual a zero, Atenção")
    else:
        print("\nFaltaram R$:", moeda(abs(restante)))
    opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")
    if opcao == "sair":
            break
