int minOperations(int* nums, int numsSize, int k) {
    int sums=0;
    for(int i=0;i<numsSize;i++){
        sums+=nums[i];
    }
    return (sums%k);
}