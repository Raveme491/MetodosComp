f(x) = x^3 - 10

a = 0
b = 10

sigma = 1e-8
num_interacao = 0


while true
    global a
    global b
    global num_interacao +=1

    c = (b+a)/2
    if f(c) == 0 || (b-a)/2 <= sigma || num_interacao >= 20
        global resultado = c
        break
    elseif f(a)*f(c) < 0
        b = c
    else
        a = c
    end
end

if num_interacao > 20
    println("Número de interações ultrapassou do limite, chute um valor mais próximo para x0")
else
    println("O valor de x que resolve a equação é ",resultado,", aproximadamente")
    println("Para encontar esse resultado foi necessário ",num_interacao, " interações")
end
