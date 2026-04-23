class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str = encoded_str+str(len(word))+"#"+word
            print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        temp_char = ""
        i=0
        while(i<len(s)):
            if s[i]!='#':
                temp_char = temp_char+s[i]
                i=i+1
            else:
                leng = int(temp_char)
                decoded_str.append(s[i+1:i+leng+1])
                i = i+1+leng
                temp_char = ""
                leng = 0
        return decoded_str


