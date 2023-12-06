class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nam = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000
                     }
        result = 0
        i = 0
        while i < len(s):
            if list(roman_nam.keys()).index(s[len(s) - i - 1]) > list(roman_nam.keys()).index(s[len(s) - i - 2]) and len(s) - i - 2 >= 0:
                # print(s[len(s) - i - 2] + s[len(s) - i - 1])
                # print(str(roman_nam[s[len(s) - i - 1]]) + ' - ' + str(roman_nam[s[len(s) - i - 2]]))
                result += roman_nam[s[len(s) - i - 1]] - roman_nam[s[len(s) - i - 2]]
                i += 1
            else:
                # print(s[len(s) - i - 1])
                # print(str(roman_nam[s[len(s) - i - 1]]))
                result += roman_nam[s[len(s) - i - 1]]
            i += 1
        return result


s = 'III'
a = Solution()
print(a.romanToInt(s))
