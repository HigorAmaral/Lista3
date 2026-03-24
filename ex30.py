temperatura = float(input('qual a temperatura que o alumínio deverá ser trabalhado: '))

if temperatura <= 500:
    print('Temperatura invalida')
elif  temperatura < 700:
    print('Aquecimento ligado em 100%')
elif temperatura < 735:
    print('Aquecimento ligado em 50%')
elif temperatura >= 735:
    print('Aquecimento desligada')
elif temperatura > 780:
    print('Superaquecimento')
else:
    print('Informe uma temperatura!!')
