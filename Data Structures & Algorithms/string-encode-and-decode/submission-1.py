class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for current in strs:
            msg += str(len(current))+'#'+current
        print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while(index!=len(s)):
            str_int = ''
            while(s[index]!='#'):
                str_int += s[index]
                index += 1
            print(str_int)
            str_int = int(str_int)
            print(s[index+1:index+str_int+1])
            result.append(s[index+1:index+str_int+1])
            index += str_int+1
        return result

            
                
            
            




