class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        c = 0
        r = len(nums) - 1

        while c <= r:
            if nums[c] == 0:
                nums[c] = nums[l]
                nums[l] = 0
                c += 1
                l += 1
            elif nums[c] == 2:
                nums[c] = nums[r]
                nums[r] = 2
                r -= 1
            else:
                c += 1