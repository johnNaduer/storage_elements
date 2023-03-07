#include <stdio.h>
#include <string.h>
char *_strcpy(char *dest, char *src);
char *_strcpy(char *dest, char *src)
{
n = strlen(src);
int i = 0
for(i = 0; i < n; i++)
{
dest[i]=src[i]
}
return (dest);
}
int main(void)
{
    char s1[98];
    char *ptr;

    ptr = _strcpy(s1, "First, solve the problem. Then, write the code\n");
    printf("%s", s1);
    printf("%s", ptr);
    return (0);
}
