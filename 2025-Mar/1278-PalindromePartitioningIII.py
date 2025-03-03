# https://leetcode.cn/problems/palindrome-partitioning-iii/description/

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        length = len(s)
        
        cost = [[0] * length for _ in range(length)]
        for width in range(2, length+1):
            for i in range(length-width+1):
                j = i + width - 1
                if s[i] == s[j]:
                    cost[i][j] = cost[i+1][j-1]
                else:
                    cost[i][j] = 1 + cost[i+1][j-1]
        
        ft = [[float('inf')] * (k + 1) for _ in range(length + 1)]
        ft[0][0] = 0
        for i in range(1, length + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    ft[i][j] = cost[0][i-1]
                else:
                    for p in range(j-1, i):
                        ft[i][j] = min(ft[p][j-1] + cost[p][i-1], ft[i][j])
        return ft[length][k]