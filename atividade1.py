# Atividade 1
# Solicita dois números float e realiza a divisão, tratando erros.

def divisao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro de divisão por zero: {zde}")
    else:
        print(f"Resultado da divisão: {resultado}")

if __name__ == "__main__":
    divisao()
    # Teste: tente digitar 0 como segundo número e também letras para testar os erros.
