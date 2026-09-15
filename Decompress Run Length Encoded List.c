int* decompressRLElist(int* nums, int numsSize, int* returnSize) {
    int total=0;
    for(int i=0;i<numsSize-1;i+=2){
        total+=nums[i];
    }
    int* arr1=(int*)malloc(total * sizeof(int));
    *returnSize = total; 
    int ind=0;
    for(int i=0;i<numsSize-1;i+=2){
        int freq = nums[i];
        int val  = nums[i + 1];
        while (freq>0) {
            arr1[ind++] = val;
            freq--;  
        }
    }
    return arr1;
}