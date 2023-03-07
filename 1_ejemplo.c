#include <stdio.h>

int get_first_element(int *list, int size) {
  // Esta función tiene una complejidad temporal O(1), ya que solo realiza
  // una operación básica (acceder al primer elemento de la lista)
  // independientemente del tamaño de la lista.
  return list[0];
}

int main() {
  int list[5] = {1, 2, 3, 4, 5};
  int first_element = get_first_element(list, 5);
  printf("El primer elemento de la lista es: %d\n", first_element);
  return 0;
}
