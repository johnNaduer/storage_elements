#include <stdio.h>

void permute(char *str, int l, int r) {
  // Esta función tiene una complejidad temporal O(n!), ya que genera
  // todas las permutaciones posibles de una cadena de tamaño n y
  // realiza una operación básica (intercambio de dos caracteres) por
  // cada permutación.
  if (l == r) {
    printf("%s\n", str);
  } else {
    for (int i = l; i <= r; i++) {
      // Intercambia el carácter en la posición l con el carácter en la
      // posición i
      char tmp = str[l];
      str[l] = str[i];
      str[i] = tmp;

      // Genera todas las permutaciones para la subcadena str[l+1, r]
      permute(str, l+1, r);

      // Restaura el carácter original en la posición l
      tmp = str[l];
      str[l] = str[i];
      str[i] = tmp;
    }
  }
}

int main() {
  char str[] = "abc";
  int n = sizeof(str) / sizeof(str[0]) - 1;
  permute(str, 0, n-1);
  return 0;
}
