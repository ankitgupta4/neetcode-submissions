class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictA = {}
        result = []
        for num in nums:
            dictA[num] = 1 + dictA.get(num,0)
        print(dictA)
        arr = [[] for i in range(len(nums)+1)]

        for key in dictA.keys():
            arr[dictA[key]].append(key)
        
        print(arr)

        for i in range(len(arr)-1, -1, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result


            

        