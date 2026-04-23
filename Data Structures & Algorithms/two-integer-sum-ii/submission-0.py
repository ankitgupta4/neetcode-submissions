class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        sum = numbers[i] + numbers[j]

        while(i<=j):
            if sum<target:
                i = i+1
                sum = numbers[i] + numbers[j]
            elif sum>target:
                j =j-1
                sum = numbers[i]+ numbers[j]
            else:
                return [i+1,j+1]
        