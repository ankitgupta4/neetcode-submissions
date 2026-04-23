class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        cnt = 0
        for num in set_nums:
            if num-1 not in set_nums:
                length = 1
                while(num+length in set_nums):
                    length += 1
                cnt = max(cnt, length)
        return cnt





            
        return final_cnt