class Solution(object):
    def decodeMessage(self, key, message):
        alphabet="abcdefghijklmnopqrstuvwxyz"
        key1={}
        j=0
        for i in key:
            if i==" ":continue
            if i not in key1:
                key1[i]=alphabet[j]
                j+=1
        decode=[]
        for i in message:
            if i==" ":decode.append(" ")
            else:decode.append(key1[i])
        return "".join(decode)