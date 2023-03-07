#include <stdio.h>

void more_numbers(void);
void more_numbers(void)
{

int i;
int m;

for(i=0;i<10;i++)
{
for(m=0;m<15;m++)
{
putchar(m+'0');
}
putchar('\n');
}
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    more_numbers();
    return (0);
}
