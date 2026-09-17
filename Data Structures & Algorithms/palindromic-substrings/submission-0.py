class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        count = 0

        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i + l -1
                if s[i] == s[j] and (l <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count


        
        