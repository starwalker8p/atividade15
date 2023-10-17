l1,l2,l3=float(input("lado 1: ")),float(input("lado 2: ")),float(input("lado 3: "))
if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    print("não é um triangulo")
else:
    print("é um triangulo")
    