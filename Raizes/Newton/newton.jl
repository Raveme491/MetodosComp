f(x) = x^3 - 10
derivada_x(x) = 3*x^2

num_interacao = 0

function newton_method(x0, sigma, n_max)
    xn = x0
    i = 0
    while i < n_max
        xn1 = xn - f(xn)/derivada_x(xn)
        if abs((xn1 - xn)/xn1) < sigma
            return xn1
        end
    xn = xn1
    i +=1
    global num_interacao += 1
    end
end

x= newton_method(2, 1e-8, 20)

println("O valor de x que resolve a equação é ",x,", aproximadamente")
println("Para encontar esse resultado foi necessário ",num_interacao, " interações")