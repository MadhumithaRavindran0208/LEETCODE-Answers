int singleNumber(int* nums, int numsSize) {
    int final=0;
    for(int i=0;i<numsSize;i++){
        final^=nums[i];
    }
    return final;
}