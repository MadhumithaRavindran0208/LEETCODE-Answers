int prefixCount(char** words, int wordsSize, char* pref) {
    int c=0;
    int pref_S=strlen(pref);
    for(int i=0;i<wordsSize;i++){
        if (strncmp(pref,words[i],pref_S)==0){
            c+=1;
        }
    }
    return c;
}