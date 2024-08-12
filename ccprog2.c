#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Numbers not specified on the command line\n");
        return 1;
    }

//dynamic allocation of memory

    int *numbers = (int *)malloc((argc - 1) * sizeof(int));

//conversion and storing of int values

    for (int i = 1; i < argc; i++) {
        numbers[i - 1] = atoi(argv[i]);
    }

//for loop to change any value over 170 to 255 and under to 0

    for (int i = 0; i < argc - 1; i++) {

    if (numbers[i] > 170) {
            printf("255 ");
        } else {
            printf("0 ");
        }
    }

    printf("\n");

    free(numbers);

}
