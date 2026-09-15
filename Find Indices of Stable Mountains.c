int* stableMountains(int* height, int heightSize, int threshold, int* returnSize) {
    int* a=(int*)malloc(heightSize*sizeof(int));
    int ind=0;
    for (int i=0;i<heightSize-1;i++){
        if(height[i]>threshold){
            a[ind]=i+1;
            ind++;
        }
    }
    *returnSize=ind;
    return a;
}