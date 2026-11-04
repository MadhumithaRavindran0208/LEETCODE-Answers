#include <string.h>
#include <stdlib.h>
void myStrrev(char* s) {
    int left=0,right=strlen(s)-1;
    while (left<right) {
        char tmp=s[left];
        s[left]=s[right];
        s[right]=tmp;
        left++;
        right--;
    }
}

char* firstPalindrome(char** words, int wordsSize) {
    for(int i=0;i<wordsSize;i++){
        char a[strlen(words[i])+1];
        strcpy(a,words[i]);
        myStrrev(a);
        if (strcmp(words[i],a)==0){
            return words[i];
        }
    }
    return "";
}