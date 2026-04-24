class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] 
        left = []
        print(left)
        right = []
        print(right)
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            left.append(prod)
        print(left)
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod = prod * nums[i]
            right.append(prod)
        
        right = right[::-1]
        print(right)
        res.append(right[1])
        for i in range(1,len(nums)-1):
            res.append(left[i-1]*right[i+1])
        res.append(left[len(nums)-2])

        return res





        