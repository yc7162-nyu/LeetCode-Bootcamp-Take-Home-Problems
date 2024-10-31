class Solution:
    def decodeString(self, s: str) -> str:
        
        st = []

        for c in s:
            if c == ']':
                curr_string = ""
                while st[-1] != '[':
                    curr_string += st.pop()
                
                # pop [
                st.pop()
                # get number
                num_string = ""
                while len(st) != 0 and '0' <= st[-1] and st[-1] <= '9':
                    num_string += st.pop()
                
                num = int(num_string[::-1])

                for i in range(num):
                    for j in range(len(curr_string) - 1, -1, -1):
                        st.append(curr_string[j])
            else:
                st.append(c)

        res = ""
        while len(st) != 0:
            res += st.pop()
        
        return res[::-1]