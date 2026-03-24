valor1 = int(input('Informe um valor de 0 a 4: '))
valor2 = 2

if valor1 == 0:
    print('A soma dos valores são', valor1 + valor2)
elif valor1 == 1:
    print('A substração dos valores é', valor1 - valor2)
elif valor1 == 2:
    print('A multiplicação dos valores é', valor1 * valor2)
elif valor1 == 3:
    print('A divisão dos valores é', valor1 // valor2)
elif valor1 == 4:
    print('A media dos valores são', valor1 + valor2 / 2)
else:
    print('Valor errado. Programa encerrado sem cálculos')

