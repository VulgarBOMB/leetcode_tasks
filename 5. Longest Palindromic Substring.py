class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s) - 1
        global_max = 0
        global_substr = ''
        if len(s) > 0:
            global_substr = s[0]
        for j in range(ln):
            # local_max = 0
            for i in range(j, ln):
                # length_subs = len(s[j:i + 2])
                print(f"{str(j)}  --  {str(i + 2)} -- {s[j:i + 2]}")
                # if length_subs == len(set(s[j:i+2])):
                #     local_max = length_subs
                # else:
                #     break
                if i + 2 - j >= global_max and self.isPalindrome(s[j:i + 2]):
                    global_max = i + 2 - j
                    global_substr = s[j:i + 2]
            # if local_max > global_max:
            #     global_max = local_max

        return global_substr

    def isPalindrome(self, x: int):
        value = str(x)
        palindrome = value[::-1]
        return True if value == palindrome else False


a = Solution()
s = "babad"
print(a.longestPalindrome(s))
