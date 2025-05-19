print("faixa etária")
ano_nascimento = int(input("coloque o ano do seu nascimento:"))
ano_atual = int(input("coloque o ano em que estamos:"))

if ano_atual <= 2025 and ano_atual >= 1908 and ano_nascimento >= 1908 and ano_nascimento <= 2025:

    idade = ano_atual - ano_nascimento

    if idade <=10:
        print(idade, "voce é criança!")
    elif idade >= 11 and idade <=  17:
        print(idade, "voce é um adolecente!")
    elif idade >= 18 and idade <=  59:
        print(idade, "voce é um adulto")
    elif idade >= 60:
        print(idade, "voce é idoso!")
else:
    print("ano invalido!")