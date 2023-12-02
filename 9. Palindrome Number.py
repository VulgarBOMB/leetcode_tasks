class Solution:
    def isPalindrome(self, x: int):
        value = str(x)
        palindrome = value[::-1]
        return True if value == palindrome else False


x = 121-121
a = Solution()
print(a.isPalindrome(x))