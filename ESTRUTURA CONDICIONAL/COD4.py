#qual numero é meior

print("saiba qual número é maior")

print("")

n1 = int(input("digite o primeiro número:"))

n2 = int(input("digite o segundo número:"))

if n1>n2:
    print(n1, "é maior que", n2)
    
elif n2>n1:
    print(n2, "é maior que", n1)
    
else:
    print(n1, "e", n2, "são iguais")