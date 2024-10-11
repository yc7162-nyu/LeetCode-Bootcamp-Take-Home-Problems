class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []
        answer.append(1)

        for i in range(1, len(nums)):
            answer.append(answer[i - 1] * nums[i - 1])

        
        multiplier = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= multiplier

            multiplier *= nums[i]
        
        return answer
    
    # Time Complexity: O(2n) => O(n)
    # Space Complexity: O(1)