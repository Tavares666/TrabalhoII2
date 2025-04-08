def verificar_comprimento(a, b):
    if len(a) != len(b):
        raise Exception("Erro: as strings têm comprimentos diferentes.")

    print("As strings têm o mesmo comprimento.")

def main():
    try:
        texto1 = input("Digite a primeira string: ")
        texto2 = input("Digite a segunda string: ")
        verificar_comprimento(texto1, texto2)
    except Exception as erro:
        print(erro)

main()
