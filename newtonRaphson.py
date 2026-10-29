
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def newton_raphson(funcao, a, repeticao):
    def f(x):
        funcoes = {"x": x,
                   "ln": math.log,
                   "log": math.log,
                   "log10": math.log10,
                   "sen": math.sin,
                   "cos": math.cos,
                   "tan": math.tan,
                   "sqrt": math.sqrt,
                   "exp": math.exp,
                   "abs": abs,
                   "pi": math.pi,
                   "e": math.e}

        expressao = funcao.replace("^", "**")
        f = eval(expressao, funcoes)
        return f

    def f_derivada(x):

        v = sp.Symbol("x")

        funcoes = {
            "x": v,
            "ln": sp.log,
            "log": sp.log,
            "log10": lambda x: sp.log(x, 10),
            "sen": sp.sin,
            "cos": sp.cos,
            "tan": sp.tan,
            "sqrt": sp.sqrt,
            "exp": sp.exp,
            "abs": sp.Abs,
            "pi": sp.pi,
            "e": sp.E
        }

        expressao = funcao.replace("^", "**")

        formula = sp.sympify(expressao, locals=funcoes)
        derivada = sp.diff(formula, v)

        return derivada.subs(v, x)

    historico = [a]
    i = 0

    while i < repeticao:
        if f_derivada(a) == 0:
            print("Derivada igual a zero!")
            return

        i += 1
        a_seguinte = a - (f(a)/f_derivada(a))
        a = a_seguinte
        historico.append(a)

    print(f"Após {repeticao} repetições, a raiz pode ser encontrada aproximadamente em {float(a)}")
    print(f"O valor final obtido na função com a raiz {float(a)} foi de {float(f(a))}")

    # ===== GRÁFICO 1: FUNÇÃO E TANGENTES =====

    x_grafico = np.linspace(
        float(min(historico)) - 1,
        float(max(historico)) + 1,
        400
    )

    y_grafico = []

    for x in x_grafico:
        try:
            y_grafico.append(float(f(x)))
        except (ValueError, ZeroDivisionError, OverflowError):
            y_grafico.append(np.nan)

    plt.figure(figsize=(10, 6))

    plt.plot(x_grafico, y_grafico, label=f"f(x) = {funcao}")
    plt.axhline(0, color="gray", linestyle="--")

    for i in range(len(historico) - 1):
        ponto = float(historico[i])
        valor = float(f(ponto))
        inclinacao = float(f_derivada(ponto))

        x_tangente = np.linspace(ponto - 0.75, ponto + 0.75, 50)
        y_tangente = valor + inclinacao * (x_tangente - ponto)

        plt.plot(x_tangente, y_tangente, "--",
                 label=f"Tangente {i + 1}")

        plt.scatter(ponto, valor)

    plt.scatter(float(a), 0, color="red",
                label="Raiz aproximada", zorder=5)

    plt.title("Método de Newton-Raphson")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()


    plt.figure(figsize=(10, 5))

    valores = [float(x) for x in historico]

    plt.plot(range(len(valores)), valores, marker="o")
    plt.axhline(float(a), color="red", linestyle="--",
                label="Aproximação final")

    plt.title("Convergência do Método de Newton-Raphson")
    plt.xlabel("Iteração")
    plt.ylabel("Aproximação da raiz")
    plt.xticks(range(len(valores)))
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


newton_raphson("x^2-2", 2, 3)
