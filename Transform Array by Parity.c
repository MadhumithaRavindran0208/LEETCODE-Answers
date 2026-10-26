int* transformArray(int* nums, int numsSize, int* returnSize) {
    int* ans=(int*)malloc(numsSize*sizeof(int));
    int* ans1=(int*)malloc(numsSize*sizeof(int));
    for (int i=0;i<numsSize;i++){
        ans[i]=nums[i]%2;
    }
    int ind=0;
    for (int i=0;i<numsSize;i++){
        if (ans[i]==0){
            ans1[ind]=0;
            ind+=1;
        }
    }
    for(int i=ind;i<numsSize;i++){
        ans1[i]=1;
    }
    free(ans);
    *returnSize=numsSize;
    return ans1;
}
int* transformArray(int* nums, int numsSize, int* returnSize) {
    int* ans=(int*)malloc(numsSize*sizeof(int));
    int ind=0;
    for (int i=0;i<numsSize;i++){
        if (nums[i]%2==0){
            ans[ind]=0;
            ind+=1;
        }
    }
    for(int i=ind;i<numsSize;i++){
        ans[i]=1;
    }
    *returnSize=numsSize;
    return ans;
}