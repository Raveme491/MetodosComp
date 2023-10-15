'''
Método que utiliza derivada para encontrar o pŕoximo valor de x
Xn+1 = Xn - f(Xn)/f'(xn)
'''

import math

def func_ref(x):
    return x*math.cos(x) - 1

def derivada(x):
    return -x*math.sin(x) + math.cos(x)

def newton_method(x0, sigma, n_max):
    xn = x0
    for n in range(n_max):
        xn1 = xn - func_ref(xn)/derivada(xn)
        if abs((xn1 - xn)/xn1) < sigma:
            return xn1, func_ref(xn1), n
        xn = xn1


result , f_result, n = newton_method(10, .00001, 20)

print(f'c:{result}\nf(c){f_result}\nn:{n}')
