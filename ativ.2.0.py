# questão 2.0
def verificar_maiusculas(nome):
    if not nome.isupper():
        raise ValueError("Erro: o nome deve conter apenas letras maiúsculas.")
    print(f"Bem-vindo ao jogo, {nome}!")



def main():
    while True:
        try:
            nome = input("Digite o nome do jogador (em letras maiúsculas): ")
            verificar_maiusculas(nome)
            break  
        except ValueError as erro:
            print(erro)
            print("Aqui está o nome corrigido:", nome.upper())
            print("Tente novamente.\n")

main()

# corrigindo commit