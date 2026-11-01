int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int *l = (int*)malloc(matrixSize * sizeof(int)); 
    for (int i = 0; i < matrixSize; i++) {
        int sum = 0;
        for (int j = 0; j < matrixColSize[i]; j++) { 
            sum += matrix[i][j];
        }
        l[i] = sum;
    }
    *returnSize = matrixSize;
    return l;
}