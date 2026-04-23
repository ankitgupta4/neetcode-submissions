class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_pro = [1 for _ in range(len(nums))]
        post_pro = [1 for _ in range(len(nums))]
        res = []
        for i in range(1, len(nums)):
            pre_pro[i] = pre_pro[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            post_pro[j] = post_pro[j+1]*nums[j+1]
        for k in range(len(nums)):
            res.append(pre_pro[k]*post_pro[k])
        return res


        