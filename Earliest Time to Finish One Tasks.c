int earliestTime(int** tasks, int tasksSize, int* tasksColSize) {
    int mini=tasks[0][0]+tasks[0][1];
    for (int i=0;i<tasksSize;i++){
        if (tasks[i][0]+tasks[i][1]<mini){
            mini=tasks[i][0]+tasks[i][1];
        }
    }
    return mini;
}