class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictA = defaultdict(int)
        for i in nums:
            dictA[i] = dictA.get(i,0) + 1
        
        print(dictA)
        arr =  [[] for _ in range(len(nums)+1)]
        print(arr)
        for key in dictA.keys():
            print(dictA[key])
            arr[dictA[key]].append(key)
            print(arr)
        res = []
        
        for l in range(len(arr)-1, -1, -1):
            print(arr[l])
            if len(arr[l])!=0:
                res.extend(arr[l])
                print(res)
                k = k-len(arr[l])
            if k==0:
                return res
        
        return res




            
            

        