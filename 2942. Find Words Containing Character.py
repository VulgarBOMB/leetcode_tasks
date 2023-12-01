# 2942. Find Words Containing Character
class Solution:

    def findWordsContaining(self, words, x):
        arr = []
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr


words = ["abc","bcd","aaaa","cbc"]
x = "a"
a = Solution()
print(a.findWordsContaining(words, x))
