class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap.keys():
                return [hashMap.get(diff), i]
            
            hashMap[nums[i]] = i


        