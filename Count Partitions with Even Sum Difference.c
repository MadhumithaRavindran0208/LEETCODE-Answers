int countPartitions(int* nums, int numsSize) {
    int count=0;
    for(int i=0;i<numsSize-1;i++){
        int d1=0,d2=0;
        for(int j=0;j<i+1;j++){
            d1+=nums[j];
        }
        for(int j=i+1;j<numsSize;j++){
            d2+=nums[j];
        }
        if ((d1+d2)%2==0){
            count+=1;
        }
    }
    return count;
}