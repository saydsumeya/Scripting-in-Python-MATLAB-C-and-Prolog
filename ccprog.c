#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Numbers not specified on the command line\n");
        return 1;
    }    

//allocate memory for an array to store the numbers

    int *numbers = (int *)malloc((argc - 1) * sizeof(int));

//for loop to convert into ints

    for (int i = 1; i < argc; i++) {
        numbers[i - 1] = atoi(argv[i]);    
    }
  
//for loop to print the values adding one

    for (int i = 0; i < argc - 1; i++) {
         numbers[i]++;
         printf("%d ", numbers[i]);
    }  
    printf("\n");

    free(numbers);
    
    return 0;
}

