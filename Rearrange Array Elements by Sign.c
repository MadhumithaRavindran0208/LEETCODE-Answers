/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int posi[numsSize];
    int nega[numsSize];
    int* final = (int*)malloc(numsSize * sizeof(int));
    int p=0, n=0;
    for(int i=0;i<numsSize;i++){
        if (nums[i]>0){
            posi[p++]=nums[i];
        }
        else{
            nega[n++]=nums[i];
        }
    }
    int j=0;
    for(int i=0;i<(numsSize/2);i++){
        final[j]=posi[i];
        final[j+1]=nega[i];
        j+=2;
    }
    *returnSize=numsSize;
    return final;
}