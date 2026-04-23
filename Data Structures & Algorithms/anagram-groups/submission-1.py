class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1_list = []
        l2_dict = []
        for strA in strs:
            dictA = defaultdict(int)
            for char in strA:
                dictA[char] += 1
            
            if dictA in l2_dict:
                l1_list[l2_dict.index(dictA)].append(strA)
            else:
                l1_list.append([strA])
                l2_dict.append(dictA)
        return l1_list

            


        