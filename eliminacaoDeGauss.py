
import numpy as np

def eliminacao_gauss(matriz):

    matriz = np.array(matriz, dtype=float)
    n = matriz.shape[0]

    if matriz.ndim != 2 or matriz.shape[1] != n + 1:
        print("Erro! Dimensões inválidas.")
        return

    print("Matriz inicial:")
    print(matriz)


    for i in range(n - 1):

        pivo = matriz[i, i]

        if abs(pivo) < 1e-12:
            print("Erro! Pivô nulo. É necessário trocar linhas.")
            return

        for j in range(i + 1, n):

            multiplicador = matriz[j, i] / pivo

            matriz[j, :] = matriz[j, :] - multiplicador * matriz[i, :]
            matriz[j, i] = 0

        print(f"\nMatriz após etapa {i + 1}:")
        print(matriz)

    resultados = np.zeros(n)

    for i in range(n - 1, -1, -1):

        if abs(matriz[i, i]) < 1e-12:
            print("Erro! O sistema não possui solução única.")
            return

        soma = 0

        for j in range(i + 1, n):
            soma += matriz[i, j] * resultados[j]

        resultados[i] = (matriz[i, -1] - soma) / matriz[i, i]

    print("RESULTADO FINAL")

    for i in range(n):
        print(f"x{i + 1} = {resultados[i]:.8f}")

    return resultados


eliminacao_gauss([
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
])
