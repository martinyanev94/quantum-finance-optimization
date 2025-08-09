#include <iostream>

const int SIZE = 1000;
int matrix[SIZE][SIZE];

void initializeMatrix() {
    for (int i = 0; i < SIZE; ++i)
        for (int j = 0; j < SIZE; ++j)
            matrix[i][j] = i + j;
}

void accessMatrixColumnWise() {
    for (int j = 0; j < SIZE; ++j)
        for (int i = 0; i < SIZE; ++i) 
            std::cout << matrix[i][j] << " ";
}

void accessMatrixRowWise() {
    for (int i = 0; i < SIZE; ++i)
        for (int j = 0; j < SIZE; ++j) 
            std::cout << matrix[i][j] << " ";
}

int main() {
    initializeMatrix();
    // accessMatrixRowWise(); // Better cache performance
    // accessMatrixColumnWise(); // Poor cache performance
    return 0;
}
