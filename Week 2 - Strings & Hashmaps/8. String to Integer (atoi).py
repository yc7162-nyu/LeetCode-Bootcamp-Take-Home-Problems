class Solution:
    def myAtoi(self, s: str) -> int:

        sstring = s.strip()

        if len(sstring) == 0:
            return 0

        # Deal with signage at the end
        # if first char is '-' then skip
        start_idx = 0
        if sstring[0] == '-' or sstring[0] == '+':
            start_idx = 1

        res = 0

        for i in range(start_idx, len(sstring)):
            if not sstring[i].isnumeric():
                break
            
            res *= 10
            res += int(sstring[i])

        if sstring[0] == '-':
            res *= -1

        return min(max(-2**31, res), 2**31 - 1)