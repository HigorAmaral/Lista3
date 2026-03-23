nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))

div = nota1 + nota2 / 2

if div >= 6:
    print('Aprovado')
else:
    print('Reprovado')