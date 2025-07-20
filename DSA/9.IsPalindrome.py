# https://leetcode.com/problems/palindrome-number/
class matching():
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]

sol = matching()

print(sol.isPalindrome(121))   # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))    # False
