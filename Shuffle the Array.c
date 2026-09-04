int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* final = (int*)malloc(numsSize * sizeof(int));
    int f=0;
    for (int i=0;i<n;i++){
        final[f]=nums[i];
        final[f+1]=nums[n+i];
        f+=2;
    }
    *returnSize = numsSize;
    return final; 
}