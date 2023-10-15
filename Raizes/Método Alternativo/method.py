"""
Aluno: Michael Soares de França
Matricula: 20220004040
Matéria:  DCA0304 - METODOS COMPUTACIONAIS EM ENGENHARIA

Atividade extra: Método para encontrar raízes
"""


def fx(x: float) -> float:
    """
    Função que se deseja encontrar a raízes o retorno dela é o f(x)
    f(x) = x³ - 10
    """
    return x**3 - 10


def yn(xn: float) -> float:
    """
    Cálculo do yn, primeiro passo do método
    o retorno dela é o yn do atual x utilizado na iteração
    """
    return xn - (2*fx(xn)**2)/(fx(xn+fx(xn)) - fx(xn-fx(xn)))


def zn(xn: float) -> float:
    """
    Cálculo do zn, segundo passo do método
    o retorno dela é o zn do atual x utilizado na iteração
    """
    return yn(xn) - fx(yn(xn))*(yn(xn) - xn)/(2*fx(yn(xn)) - fx(xn))


def xn1(xn: float) -> float:
    """
    Cálculo do xn+1, equação para encontrar o próximo valor
    de para convergir para a raíz
    """
    return zn(xn) - fx(zn(xn))*(yn(xn) - xn)/(2*fx(yn(xn)) - fx(xn))


def metodo(x0: float) -> (float, int):
    """
    Função criada para organizar a estrutura do método e
    melhorar a modularização do código

        ***Variáveis***
    x0 -> Chute inicial
    novo_x -> valor atualizado do x para determinada iteração
    sigma -> Grau de precisão
    contador -> Número de iterações necessárias para convergir
    """

    novo_x = x0
    sigma = 1e-13
    contador = 0

    while sigma <= abs(fx(novo_x)) and contador < 20:
        novo_x = xn1(x0)
        x0 = novo_x  # atualizção dos valores
        contador += 1

    return novo_x,  contador


def validador(x0, x_final, iteracoes):
    """
    Função dedicada a tratar possíveis divergências de valores a partir de um
    chute muito distante da raíz da função
    """
    print("\n")
    print("Resultados:")
    if abs(fx(x0)) < abs(fx(x_final)):
        print("Valor não convergiu")
        print("Por favor, tente chutar um valor mais próximo da raíz")
    else:
        print("O valor de X é {:.13f}".format(x_final))
        print('O valor de f(x) para x encontrado é {:.13f}'.format(fx(x_final)))
        print(f'Foram necessárias {iteracoes} iterações para o valor convergir')


if __name__ == '__main__':
    print("Método para encontrar raízes da função f(x) = x³ - 10")
    print("Este método é limitado pelo valor inicial de X, busque pôr um chute inicial próximo ao valor da raízes para que convirja")
    print("-------------")
    try:
        valor_inicial = float(input("Forneça um valor inicial para X: "))
        resultado_x, n_interacoes = metodo(valor_inicial)
        validador(valor_inicial, resultado_x, n_interacoes)
    except ValueError:
        print("É necessário que seja digitado um valor válido")
