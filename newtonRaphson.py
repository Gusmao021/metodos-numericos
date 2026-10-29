import math
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
        f = eval(expressao,funcoes)
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
    
    i = 0
    while i < repeticao:
        if f_derivada(a) == 0:
            print(f"A derivada da função {funcao} é 0 portanto não pode ser resolvida com o metodo newton_raphson")
            quit()
            
        i += 1
        a_seguinte = a - (f(a)/f_derivada(a))
        a = a_seguinte

    print(f" Após {repeticao} repetições, a raiz pode ser encontrada aproximadamente em {float(a)}")  

newton_raphson("x^2-2", 2, 3)