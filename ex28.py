salario = float(input("Digite o salário atual: "))

if salario <= 400:
    percentual = 0.15
elif salario <= 700:
    percentual = 0.12
elif salario <= 1000:
    percentual = 0.10
elif salario <= 1500:
    percentual = 0.07
elif salario <= 2000:
    percentual = 0.04
else:
    percentual = 0

aumento = salario * percentual
novo_salario = salario + aumento

print("Percentual de aumento:", percentual * 100, "%")
print("Novo salário:", novo_salario)