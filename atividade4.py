# Atividade 4
# Função que agrupa elementos de duas listas em tuplas de 3 elementos, com tratamento de erros.

def agrupa_listas(lista1, lista2):
    try:
        if len(lista1) != len(lista2):
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
        resultado = []
        for i in range(len(lista1)):
            resultado.append((lista1[i], lista2[i], lista1[i] + lista2[i]))
        return resultado
    except Exception as e:
        print(f"Erro: {type(e).__name__} - {e}")
        return None

if __name__ == "__main__":
    # Testes
    print(agrupa_listas([4,6,7,9,10], [-4,6,8,7,9]))
    print(agrupa_listas([4,6,7,9,10,4], [-4,6,8,7,9]))
    print(agrupa_listas([4,6,7,9,'A'], [-4,'E',8,7,9]))
