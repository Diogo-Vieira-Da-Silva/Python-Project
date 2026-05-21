# Atividade 2
# Solicita um nome e busca no dicionário, tratando KeyError.

def busca_idade():
    idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
    chave = input("Digite o nome a ser pesquisado: ")
    try:
        valor = idades[chave]
    except KeyError:
        print("Nome não encontrado")
    else:
        print(f"Idade: {valor}")

if __name__ == "__main__":
    busca_idade()
    # Teste: digite um nome presente e um ausente para ver o tratamento.
