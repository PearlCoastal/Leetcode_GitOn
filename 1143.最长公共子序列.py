#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        A, B = len(text1), len(text2)
        dp = [[0 for i in range(B + 1)] for j in range(A + 1)]

        for i in range(1, A + 1):
            for j in range(1, B + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
        return dp[A][B]

# @lc code=end

text1 = "abcde"
text2 = "ace" 

ob = Solution()
ans = ob.longestCommonSubsequence(text1, text2)
ans