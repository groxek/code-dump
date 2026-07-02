class Solution:
    def reverseString(self, s: list[str]) -> None:
        l = 0
        r = len(s) - 1

        while r > l:
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1


sol = Solution()
print(sol.reverseString(["h", "e", "l", "l", "o"]))
