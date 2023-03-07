#include <stdio.h>

int sum_elements(int *list, int size) {
  // Esta función tiene una complejidad temporal O(n), ya que itera sobre
  // todos los elementos de la lista y realiza una operación básica
  // (suma) por cada elemento.
  int sum = 0;
  for (int i = 0; i < size; i++) {
    sum += list[i];
  }
  return sum;
}

int main() {
  int list[5] = {1, 2, 3, 4, 5};
  int sum = sum_elements(list, 5);
  printf("La suma de todos los elementos de la lista es: %d\n", sum);
  return 0;
}
