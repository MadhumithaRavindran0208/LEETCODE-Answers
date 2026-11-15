int diagonalSum(int** mat, int matSize, int* matColSize) {
    int s=0;
    for(int i=0;i<matSize;i++){
        s+=mat[i][i];
        s+=mat[i][matSize-1-i];
    }
    if(matSize%2==1){s-=mat[matSize/2][matSize/2];}
    return s;
}