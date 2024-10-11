class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum == target:
                break
            elif currSum < target:
                l += 1
            else:
                r -= 1
        
        return [l + 1, r + 1]
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)