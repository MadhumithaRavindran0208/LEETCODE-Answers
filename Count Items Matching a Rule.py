class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rule=["type","color","name"]
        ind=rule.index(ruleKey)
        final=0
        for i in range(len(items)-1,-1,-1):
            a=items[i]
            if a[ind]==ruleValue:final+=1
        return final
        