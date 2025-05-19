#função int
def input_int(recado):
    while True:
        try:
            valor = int(input("digite um número: "))
            return valor  
        except ValueError:  
            print("\033[0;30;41mERRO!\033[m")
            print("insira um número válido.")  




#função float
def input_float(recado):
    while True:
        try:
            valor = float(input("digite um número: "))  
            return valor  
        except ValueError:  
            print("\033[0;30;41mERRO!\033[m")
            print("insira um número válido.")  




#função str
def input_str(recado):
    while True:
        try:
            valor = input("digite um texto: ")  
            if not valor:  
                raise ValueError("Entrada não pode ser vazia.")  
            return valor  
        except ValueError:  
            print("\033[0;30;41mERRO!\033[m")
            print("insira um texto válido.")  
