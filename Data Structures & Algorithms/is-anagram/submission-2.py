class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictA = defaultdict(int)
        dictB = defaultdict(int)
        for char in s:
            dictA[char]+=1
        for char in t:
            dictB[char]+=1

        if dictA==dictB:
            return True
        return False
        