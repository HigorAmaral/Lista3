hor1 = int(input('Informe as horas de aulas dadas'))
hor2 = int(input('Informe as horas de aulas dadas'))
valor1 = float(input('Informe o valor da hora de trabalho'))
valor2 = float(input('Informe o valor da hora de trabalho'))

salario1 = hor1 * valor1
salario2 = hor2 * valor2

if salario1 > salario2:
    print('O primeiro professor recebeu mais')
elif salario2 > salario1:
    print('O segundo professor recebeu mais')
else:
    print('Os professores receberam o mesmo valor')