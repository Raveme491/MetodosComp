/*
  O método aqui é exatamente o mesmo utilizado nas outras linguagens,
  o que muda é a necessidade de utilização de pointeiros na função final do método
  tendo em vista a necessidade do retorno de múltiplas variáveis
*/

#include <stdio.h>
#include <math.h>

double fx(double x){
  return x*x*x - 10;
}

double y_n(double xn){
  return xn - (2*fx(xn)*fx(xn))/(fx(xn+fx(xn)) - fx(xn - fx(xn)));
}

double zn(double xn){
  return y_n(xn) - fx(y_n(xn))*(y_n(xn) - xn)/(2*fx(y_n(xn)) - fx(xn));
}

double xn1(double xn){
    return zn(xn) - fx(zn(xn))*(y_n(xn) - xn)/(2*fx(y_n(xn)) - fx(xn));
}

void calculo_raiz(float x0, int* contador, double* resultado){
  double sigma = 1e-13;
  while (sigma<(fabs(fx(*resultado))) && *contador < 20 ) {
    *resultado = xn1(x0);
    x0 = *resultado;
    (*contador)++;
  }
  }

int main(void) {
  int contador = 0;
  float x0 = 2;
  double resultado;

  calculo_raiz(x0, &contador, &resultado);

  printf("O valor de X que melhor se aproxima da raíz é %.13f \n", resultado);
  printf("Para esse valor de x, f(x) é: %.13f, aproximadamente \n", fx(resultado));
  printf("Foram necessárias %d iterações para o resultado convergir\n", contador);
  return 0;
}
