def fib(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])


# print(fib(7))
string = 'porprop'
# string = 'paap'
n = len(string)
print(palindrome(string))

# 4 - 2   [1:2]
# 5 - 2,5 [1:3]
#
# i
# n - i - 1
