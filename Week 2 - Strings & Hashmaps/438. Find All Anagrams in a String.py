class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # Sliding window and hashmaps to store elements in the hashmap

        p_hmap = {}
        for c in p:
            if c in p_hmap:
                p_hmap[c] += 1
            else:
                p_hmap[c] = 1
        
        l = 0
        window_hmap = {}

        res = []

        for r in range(0, len(s)):
            if s[r] in window_hmap:
                window_hmap[s[r]] += 1
            else:
                window_hmap[s[r]] = 1
            
            # Anagram if hmaps are equal
            if window_hmap == p_hmap:
                res.append(int(l))
            
            if r - l + 1 == len(p):
                window_hmap[s[l]] -= 1
                if window_hmap[s[l]] == 0:
                    window_hmap.pop(s[l])
            
                l += 1
        
        return res

        # Time Complexity: O(len(s))
        # Space Complexity: O(2K) where k is unique chars in p => O(1)