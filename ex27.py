opcao = int(input("Digite a opção (1, 2 ou 3): "))
a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

valores = [a, b, c]

if opcao == 1:
    valores.sort()
    print("Ordem crescente:", valores)

elif opcao == 2:
    valores.sort(reverse=True)
    print("Ordem decrescente:", valores)

elif opcao == 3:
    valores.sort()
    print("Ordem com maior no meio:", valores[0], valores[2], valores[1])

else:
    print("Opção inválida")