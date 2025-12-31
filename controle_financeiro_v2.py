def moeda(valor):
    texto = f"{valor:,.2f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")

def ler_valor(msg):
    valor = input(msg)
    valor = valor.replace(",", ".")
    return float(valor)

def main():
    print("\n=== CONTROLE FINANCEIRO ===\n")

    salario = ler_valor("Digite seu Salário: ")

    gastos = {}
    gastos["Aluguel"] = ler_valor("Aluguel: ")
    gastos["Energia"] = ler_valor("Energia: ")
    gastos["Água"] = ler_valor("Água: ")
    gastos["Internet"] = ler_valor("Internet: ")
    gastos["Cartão"] = ler_valor("Cartão: ")
    gastos["Assinaturas"] = ler_valor("Assinaturas: ")

    print("\nGastos informados: ")
    for nome, valor in gastos.items():
        porcentagem = (valor / salario) * 100
        print(f" -{nome}: R$ {moeda(valor)} ({porcentagem:.1f}%)")
    total_gastos = sum(gastos.values())

    saldo = salario - total_gastos

    print("\nResumo:")
    print("Salário: R$", moeda(salario))
    print("Total de Gastos: R$", moeda(total_gastos))

    if saldo >0:
        print("Saldo Restante: R$", moeda(saldo))
        print("Boa! Sobrou Dinheiro 😁")

    elif saldo ==0:
        print("Saldo zerado, Atenção")

    else:
        print("Faltaram: R$", moeda(abs(saldo)))
        print("Atenção, Gastos maiores do que a Renda❌")
main()
