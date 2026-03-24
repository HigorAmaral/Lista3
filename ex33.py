idadeh1 = int(input('Informe a idade de um homem: '))
idadeh2 = int(input('Informe a idade de outro homem: '))
idadem1 = int(input('Informe a idade de uma mulher: '))
idadem2 = int(input('Informe a idade de outra mulher: '))

if idadeh1 > idadeh2:
    homem_velho = idadeh1
    homem_novo = idadeh2
else:
    homem_velho = idadeh2
    homem_novo = idadeh1

if idadem1 > idadem2:
    mulher_velha = idadem1
    mulher_nova = idadem2
else:
    mulher_velha = idadem2
    mulher_nova = idadem1

soma = homem_velho + mulher_nova
produto = homem_novo * mulher_velha

print('Soma:', soma)
print('Produto:', produto)