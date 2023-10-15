## Método utilizado para encontrar a raíz

A função fornecida foi:

$$
\begin{equation}
    f(x) = x^{3} - 10
\end{equation}
$$

O método utilizado utiliza 3 equações consecutivas de forma iterativa para aproximar o próximo valor de X, fazendo com que a função convirja para o valor de $f(x) = 0$.

As equações fornecidas foram as seguintes:

$$
\begin{equation}
    y_{n} = x_{n} - \frac{2f(x_{n})^2}{f(x_{n} +f(x_{n})) - f(x_{n} - f(x_{n}))}
\end{equation}
$$

$$
\begin{equation}
    z_{n} = y_{n} - \frac{y_{n} - x_{n}}{2f(y_{n}) - f(x_{n})}f(y_{n})
\end{equation}
$$

$$
\begin{equation}
    x_{n+1} = z_{n} - \frac{y_{n} - x_{n}}{2f(y_{n})-f(x_{n})}f(z_{n})
\end{equation}
$$

Esse método se apresenta como uma melhoria substâncial em relação ao método de newton e o da secante, tendo em vista uma maior a ausência de necessidade da derivada e da secante nos pontos. Por outro lado, analiticamente ele possui um grau de divergência relavante quando o valor inicial fornecido é muito distante da raíz do polinômio.



Observando o comportamento da função, é perceptível que a raíz é tal que:

$$
 \begin{equation} 
     x = \sqrt[3]{10} \cong 2,1544346900319
 \end{equation}
$$

Para resolução desse problema, foram utilizadas 3 linguagens que são normalmente utilizadas em computação numérica:

1. `Python v3.11.4`
2. `C`
3. `Julia v1.9.3`


Com o objetivo de comparar o grau de dificuldade na escrita do código-fonte e na velocidade de obtenção da resposta. Para as três linguagens, a resposta do valor de x foi 2.1544346900319, padronizando a precisão de 13 casas decimais. Para uma precisão com mais casas decimais, talvez o valor divirja um pouco nas últimas, mas nada substâncial para prejudicar a análise.

## Comparativo entre linguagens

Para avaliar o tempo de execução do código em Python foi utilizado a biblioteca time. Para o código em C, foi utilizada a biblioteca time.h. Já para Júlia, foi utilizada uma função interna que executa uma parte do código e verifica o tempo. Após rodar os códigos em cada linguagem, encontrou-se os seguintes resultados:

1. `C`: 2 $\mu$s
2. `Julia`: 100 $$\mu$$s
3. `Python`: 104 $$\mu$$s
$$\mu$$