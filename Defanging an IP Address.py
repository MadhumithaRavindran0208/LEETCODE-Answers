class Solution(object):
    def defangIPaddr(self, address):
        final=""
        for i in address:
            if i==".":
                final+="[.]"
            else:final+=i
        return final                
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")