time1 = input('Informe o nome do time 1: ')
time2 = input('Informe o nome do time 2: ')
gol1 = int(input('Informe a quantidade de gols do time 1: '))
gol2 = int(input('Informe a quantidade de gols do time 2: '))

if gol1 > gol2:
    print('Time 1 ganhou', time1)
elif gol2 > gol1:
    print('Time 2 ganhou,', time2)
else:
    print('Empate')

