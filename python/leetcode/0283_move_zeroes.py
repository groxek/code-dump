class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] != 0:
                l += 1
            elif nums[r] == 0:
                r += 1


sol = Solution()
print(sol.moveZeroes([4,2,4,0,0,3,0,5,1,0]))
