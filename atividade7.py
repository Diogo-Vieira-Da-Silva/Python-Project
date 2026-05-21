# Atividade 7
# Função que divide elementos de duas listas, tratando ValueError e ZeroDivisionError.

def divide_colunas(pressoes, temperaturas):
    try:
        if len(pressoes) != len(temperaturas):
            raise ValueError('As listas devem ter o mesmo tamanho.')
        resultado = []
        for p, t in zip(pressoes, temperaturas):
            resultado.append(p / t)
        return resultado
    except ZeroDivisionError:
        print('Erro: Divisão por zero encontrada.')
        return None
    except ValueError as ve:
        print(f'Erro: {ve}')
        return None

if __name__ == "__main__":
    # Testes
    pressoes1 = [100, 120, 140, 160, 180]
    temperaturas1 = [20, 25, 30, 35, 40]
    print(divide_colunas(pressoes1, temperaturas1))

    pressoes2 = [60, 120, 140, 160, 180]
    temperaturas2 = [0, 25, 30, 35, 40]
    print(divide_colunas(pressoes2, temperaturas2))

    pressoes3 = [100, 120, 140, 160]
    temperaturas3 = [20, 25, 30, 35, 40]
    print(divide_colunas(pressoes3, temperaturas3))
