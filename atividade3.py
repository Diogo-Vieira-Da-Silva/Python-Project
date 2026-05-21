# Atividade 3
# Função que converte todos os valores de uma lista para float, com tratamento de erro e finally.

def converte_lista(lista):
    try:
        nova_lista = [float(x) for x in lista]
    except Exception as e:
        print(f"Erro: {type(e).__name__} - {e}")
        return None
    else:
        return nova_lista
    finally:
        print("Fim da execução da função")

if __name__ == "__main__":
    print(converte_lista([1, 2, 3]))
    print(converte_lista([1, 'a', 3]))
