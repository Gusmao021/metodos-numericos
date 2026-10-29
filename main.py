import math

def falsa_posicao(funcao, a, b, erro_aceitavel):

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
        f = eval(expressao,funcoes)
        return f

    i = 0
    c_anterior = 0
    c = (a*f(b) - b*f(a))/(f(b)-f(a)) #calcular a secante
    erro = abs(c - c_anterior)
     
    while erro > erro_aceitavel:
        
        c_posterior = (a*f(b) - b*f(a))/(f(b)-f(a))

        if f(a) * f(b) >= 0:
            print("Erro! Mais de uma raiz presente ou nenhuma raiz presente")
            quit()

        elif f(c_posterior) * f(a) < 0:
            erro = abs(c_posterior - b)
            b = c_posterior
            i += 1
        
        elif f(c_posterior) * f(b) < 0:
            erro = abs(c_posterior - a)
            a = c_posterior
            i += 1
        
        else:
            print("Algo deu errado!")
            quit()
        
    
    print(f"A taxa de erro após {i} iteraçõe(s) é de {erro}")
    print(f"A raiz pode ser encontrada aproximadamente em {c_posterior}")
    print(f"O limite inferior encontrado é {a} e o limite superior é {b}")

falsa_posicao("ln(x) + x - 2", 1, 2, 0.001)
falsa_posicao("cos(x) - x", 0, 1, 0.001)
falsa_posicao("e^x - 3*x", 0, 1, 0.001)