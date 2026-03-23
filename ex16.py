meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

numero = int(input("Digite um número de 1 a 12: "))

if 1 <= numero <= 12:
    print("Mês correspondente:", meses[numero - 1])
else:
    print("Número inválido!")