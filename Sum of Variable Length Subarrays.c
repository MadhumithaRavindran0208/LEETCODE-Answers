int subarraySum(int* nums, int numsSize) {
    int final=0,start=0;
    for(int i=0;i<numsSize;i++){
        if (i-nums[i]>0){
            start=i-nums[i];
        }
        else{
            start=0;
        }
        for(int j=start;j<i+1;j++){
            final+=nums[j];
        }
    }
    return final;
}