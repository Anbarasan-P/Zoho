class Solution():
    def isMatch(self, s: str, p: str):
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m +1)]


        dp[0][0] = True

        for j in range(1, n+1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j -1] == s[i - 1] or p[j -1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j -1] =='*':
                    dp[i][j] = dp[i][j-1] or dp[i - 1][j]


        return dp[m][n]
    
Sol = Solution()

print(Sol.isMatch("aa", "a"))     # False
print(Sol.isMatch("aa", "*"))     # True
print(Sol.isMatch("cb", "?a"))    # False
print(Sol.isMatch("adceb", "*a*b")) # True
