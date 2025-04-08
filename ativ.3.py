def dividir_por(numero):

    if numero == 0:
        
        raise ZeroDivisionError("Erro: não é possível dividir por zero.")
    resultado = 10 / numero
    print("Resultado da divisão:", resultado)


def main():
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        try:
            num = int(entrada)
            dividir_por(num)
        except ZeroDivisionError as erro:
            print(erro)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair'.")

        print()  
main()
# corrigindo commit

