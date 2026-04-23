class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictA = {}
        for num in nums:
            if num in dictA:
                return True
            dictA[num] = 1

        return False



        