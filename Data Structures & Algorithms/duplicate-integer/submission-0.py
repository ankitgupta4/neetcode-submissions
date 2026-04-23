class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap_array = {}
        for num in nums:
            if num not in hashmap_array:
                hashmap_array[num]=1
            else:
                return True
        return False


         