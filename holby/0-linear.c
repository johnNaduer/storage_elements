#include <stdio.h>
#include <stdlib.h>
#include "search_algos.h"

int linear_search(int *array, size_t size, int value)
{

size_t i;

if(array == NULL)
{
return (-1);
}
for(i = 0; i < size; i++)
{
printf("value checked array[%ld] = [%d]\n",i,array[i]);
if(array[i]==value)
{
break;
}
}
if(array[i]==value)
{
return (i);
}
else
{
return (-1);
}
}
