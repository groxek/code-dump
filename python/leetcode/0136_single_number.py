# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         return sum(set(nums))*2 - sum(nums)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))