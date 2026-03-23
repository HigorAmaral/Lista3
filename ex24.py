a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Digite o código da operação: "))

if op == 1:
    resultado = a + b
elif op == 2:
    resultado = a - b
elif op == 3:
    resultado = a * b
elif op == 4:
    if b != 0:
        resultado = a / b
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)