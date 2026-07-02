class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers)-1

        while r>l:
            now = numbers[l]+numbers[r]
            if now > target:
                r -= 1
            elif now < target:
                l +=1
            else:
                return [l+1, r+1]
  
            
numbers = [-1,0]
target = -1
sol = Solution()
print(sol.twoSum(numbers, target))