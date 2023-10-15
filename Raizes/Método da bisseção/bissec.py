'''
Algoritmo para encontrar o zero da função a partir do método da bissecção
'''
import math


def funcao_ref(x):
    return x*math.cos(x) - 1


def muda_sinal(x0, h):
    while funcao_ref(x0) * funcao_ref(x0+h) > 0:
        x0 += h
    a = x0
    b = x0 + h

    return a, funcao_ref(a), b, funcao_ref(b)


a, fa, b, fb = muda_sinal(0, 0.0001)


def precissao(a, b, sigma):
    return math.ceil(math.log2(b-a) - math.log2(sigma))


def bissec(a,b, sigma):
    n = 1
    n_max = precissao(a, b, sigma)
    while n <= n_max:
        c = (a+b)/2
        if funcao_ref(c) == 0 or (b-a)/2 < sigma:
            return c, funcao_ref(c), n
        elif funcao_ref(a)*funcao_ref(c) < 0:
            b = c
        else:
            a = c
        n += 1

c, fc, n = bissec(a, b, math.pow(10, -5))

print(f'c:{c}\nf(c){fc}\nn:{n}')
