class Solution:
    def reverseWords(self, s: str) -> str:
        
        s.strip()

        res = ""
        curr = ""

        for i in range(len(s) - 1, -2, -1):

            if len(curr) == 0 and (s[i] == ' ' or i < 0):
                continue
            
            if i == -1 or s[i] == ' ':
                res += curr[::-1]
                res += ' '

                curr = ''
            else:
                curr += s[i]
        
        return res[:-1]