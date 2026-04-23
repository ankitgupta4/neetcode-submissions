class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictA = {}
        for i in range(len(nums)):
            if target-nums[i] in dictA:
                return [dictA[target-nums[i]],i]
            else:
                dictA[nums[i]] = i