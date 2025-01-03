#include <stdio.h>

void main() {
    int num;
    printf("enter the number: \n");
    scanf("%d", &num);
    
    int total = 0;
    
    for (int i = 0; i <= num; i++)
    {
         total += 1;
         printf("%d \n", total);
    }
}