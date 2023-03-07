#include <stdio.h>

void print_pairs(int *list, int size) {
  // Esta función tiene una complejidad temporal O(n^2), ya que itera
  // sobre todos los pares de elementos de la lista y realiza una
  // operación básica (impresión por pantalla) por cada par.
  for (int i = 0; i < size; i++) {
    for (int j = i+1; j < size; j++) {
      printf("(%d, %d)\n", list[i], list[j]);
    }
  }
}

int main() {
  int list[5] = {1, 2, 3, 4, 5};
  print_pairs(list, 5);
  return 0;
}
