class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for charS in s:
            if charS in dictS:
                dictS[charS] += 1
            else:
                dictS[charS] = 1
        for charT in t:
            if charT in dictT:
                dictT[charT] += 1
            else:
                dictT[charT] = 1
        print(dictS)
        print(dictT)
        
        if dictS != dictT:
            return False
        return True



        
        