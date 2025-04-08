class Numeroimparerror(Exception):
    def __init__(self,numero):  
        super().__init__(f"O número {numero} é ímpar. Por favor, digite um número par.")

def verificar_par(numero):
    if numero % 2 != 0:
        raise Numeroimparerror(numero)
    else:
        print(f"O número {numero} é par.")
        
def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            verificar_par(numero)
            break 
        except Numeroimparerror as e:
            print(f"Erro: {e}")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()

