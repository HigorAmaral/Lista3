salario = float(input('Informe o seu salario: '))

if salario < 10000:
    print('O seu salario tera um reajuste de 55%', salario + salario * 0.55)
elif salario >=1000 and  salario <= 25000:
    print('O seu salario tera um reajuste de 20%', salario + salario * 0.20)
else:
    print('O seu salario tera um reajuste de 20%', salario + salario * 0.20)