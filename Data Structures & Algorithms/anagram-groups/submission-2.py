class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        resultDict = []
        for i in range(len(strs)):
            charDict = defaultdict(int)
            for char in strs[i]:
                charDict[char]+=1
            print("String", strs[i], " Dictionary", charDict)
            if charDict in resultDict:
                ind = resultDict.index(charDict)
                result[ind].append(strs[i])
                print("Appended ", strs[i], "at ", ind)
            else:
                result.append([strs[i]])
                resultDict.append(charDict)
                print("New Append", strs[i])
        return result





                



        