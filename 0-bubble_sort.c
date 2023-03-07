#include "sort.h"

/**
 * swap_pos - swaps position of values in array
 *
 * @array: array to be changed
 * @first: first index
 * @second: second index
 */
void swap_pos(int **array, size_t first, size_t second)
{
	int h_s;

	h_s = (*array)[first];
	(*array)[first] = (*array)[second];
	(*array)[second] = h_s;
}

/**
 * bubble_sort - sorting algorithm that sorts in form
 * of a bubble
 *
 * @array: array to be sorted
 * @size: size of the array
 */
void bubble_sort(int *array, size_t size)
{
	size_t n, m, g;

	if (size < 2)
		return;

	for (n = 0; n < size; n++)	/* go through the array */
	{
		g = 0;
		for (m = 0; m < size - n - 1; m++)	/* loop only the unsorted */
		{
			if (array[m] > array[m + 1])
			{
				swap_pos(&array, m, m + 1);
				print_array(array, size);
				g = 1;
			}
		}

		/* check if no swap occured (meaning array is sorted) */
		if (!g)
			break;
	}
}
