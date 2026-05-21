# Atividade 6
# Função que verifica se há pontuação em palavras de uma lista, lançando ValueError se houver.

def verifica_pontuacao(lista):
    for palavra in lista:
        if (',' in palavra) or ('.' in palavra) or ('!' in palavra) or ('?' in palavra):
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    print("Nenhuma pontuação encontrada.")

if __name__ == "__main__":
    lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
    lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
    try:
        verifica_pontuacao(lista_tratada)
    except ValueError as ve:
        print(ve)
    try:
        verifica_pontuacao(lista_nao_tratada)
    except ValueError as ve:
        print(ve)
