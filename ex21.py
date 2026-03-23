a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

soma = a + b + c - menor
print("Soma dos dois maiores:", soma)