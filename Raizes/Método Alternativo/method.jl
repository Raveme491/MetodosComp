# Função f(x) que se deseja encontrar a raíz
f(x) = x^3 - 10 

# Cálculo para calcular o valor de yn para a determinada iteração
y(x) = x - 2*f(x)^2/(f(x + f(x))- f(x - f(x))) 

# Cálculo para encontrar o valor de zn para determinada iteração
z(x) = y(x) - f(y(x))*(y(x) - x)/(2*f(y(x)) - f(x)) #

# Cálculo para encontrar o valor de xn+1, ou seja, o próximo valor de x
x1(x) = z(x) - f(z(x))*(y(x) - x)/(2*f(y(x)) - f(x))

function main()
        # Grau de Precisão exigido
        sigma  = 1e-13 
        num_interacoes = 0 
        xn = 2
        # Chute inicial
        let x0 = 2
        # Contador de iterações
        while sigma <= abs(f(xn)) && num_interacoes<20
            #Esse valor de iterações limita possíveis loops infinitos por divergencia dos resultados
            xn = x1(x0)
            x0 = xn
            num_interacoes+=1
        end
    
        if num_interacoes > 20
            println("Número de interações ultrapassou do limite, chute um valor mais próximo para x0")
        else
            println("O valor de x que resolve a equação é ",round(xn,digits= 13),", aproximadamente")
            println("Para encontar esse resultado foi necessário ",num_interacoes, " interações")
        end
    end
    end

main()