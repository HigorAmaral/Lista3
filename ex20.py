a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a > b and a > c:
    print("Maior:", a)
elif b > a and b > c:
    print("Maior:", b)
else:
    print("Maior:", c)