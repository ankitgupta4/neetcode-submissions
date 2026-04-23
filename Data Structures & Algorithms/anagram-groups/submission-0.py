class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op_dict_array = defaultdict(list)
        for word in strs:
            currArr = [0]*26
            for char in word:
                currArr[ord(char) - ord('a')] += 1
            op_dict_array[tuple(currArr)].append(word)
        return list(op_dict_array.values())
            
            


        