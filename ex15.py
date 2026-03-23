valor = float(input('Informe o valor do produto'))

if valor <= 20:
    print('O produto sera vendido por', valor + valor * 0.45)
else:
    print('O produto sera vendido por', valor + valor * 0.30)
