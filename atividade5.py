# Atividade 5
# Código para contabilizar pontuações de estudantes em um teste, com tratamento de ValueError.

def calcula_notas(gabarito, respostas):
    try:
        for teste in respostas:
            for alt in teste:
                if alt not in ['A', 'B', 'C', 'D']:
                    raise ValueError(f"A alternativa {alt} não é uma opção de alternativa válida")
        notas = []
        for teste in respostas:
            nota = sum([1 for i, alt in enumerate(teste) if alt == gabarito[i]])
            notas.append(nota)
        return notas
    except ValueError as ve:
        print(ve)
        return None

if __name__ == "__main__":
    gabarito = ['D', 'A', 'B', 'C', 'A']
    testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
    testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
    print(calcula_notas(gabarito, testes_sem_ex))
    print(calcula_notas(gabarito, testes_com_ex))
