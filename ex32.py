valor1 = int(input("Informe um numero: "))
valor2 = int(input("Informe outro numero: "))

resto = valor1 % valor2

if resto == 1:
    print("Resultado:", valor1 + valor2 + resto)

elif resto == 2:
    if valor1 % 2 == 0:
        print("valor1 é Par")
    else:
        print("valor1 é Ímpar")

    if valor2 % 2 == 0:
        print("valor2 é Par")
    else:
        print("valor2 é Ímpar")

elif resto == 3:
    print("Resultado:", (valor1 + valor2) * valor1)

elif resto == 4:
    if valor2 != 0:
        print("Resultado:", (valor1 + valor2) / valor2)
    else:
        print("Não é possível dividir por zero")

else:
    print("Quadrado de valor1:", valor1**2)
    print("Quadrado de valor2:", valor2**2)
