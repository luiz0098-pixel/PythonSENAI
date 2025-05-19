#qual dos tres numeros é maior 

print("qual dos três números é o maior?")
n1 = int(input("digite o primeiro número:"))
print("")
n2 = int(input("digite o segundo número:"))
print("")
n3 = int(input("digite o terceiro número:"))
print("")
if n1>n2:
    if n1>n3:
        print(n1, "é o maior número")
    elif n3>n2:
        print(n3, "é o maior numero")
    elif n2>n3:
        print(n2, "é o maior numero")
    else:
        print(n3, "é o maior numero")
        