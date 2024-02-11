import math


class Solution:
    def isPalindrome(self, x: int):
        value = str(x)
        palindrome = value[::-1]
        return True if value == palindrome else False

    def isRealPalindrome(self, str_line):
        len_of_str = len(str_line)
        if len_of_str == 0:
            return False
        elif len_of_str == 1:
            return True
        elif len_of_str % 2 == 0:
            dict = self.searchChar(str_line)
            for amount in dict.values():
                if amount % 2 == 1:
                    return False
            return True
        else:
            dict = self.searchChar(str_line)
            odd_count = sum(1 for count in dict.values() if count % 2 != 0)
            return True if odd_count <= 1 else False

    def searchChar(self, str_line: str):
        dict = {}
        set_of_chars = set(str_line)
        for char in set_of_chars:
            dict[char] = str_line.count(char)
        return dict


# x = 1234
# line = '1222331'
# a = Solution()
# # print(a.isPalindrome(x))
# print(a.isRealPalindrome(line))


arr = [9, 1, 2, 7, 1, 5, 7, 9, 2]

# dict = {}
# for item in arr:
#     dict[item] = arr.count(item)
# print(list(dict.keys())[list(dict.values()).index(1)])

unpaired = 0
for number in arr:
    print(unpaired)
    unpaired ^= number
    print(unpaired)
    print('---------')
print(unpaired)
