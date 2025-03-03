# https://leetcode.cn/problems/palindrome-partitioning-ii/description/


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pali_map = [[True] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                pali_map[i][j] = (s[i] == s[j]) and pali_map[i+1][j-1]
        
        cut_f = [x for x in range(n)]
        for i in range(n):
            if pali_map[0][i]:
                cut_f[i] = 0
            else:
                for j in range(i):
                    if pali_map[j+1][i]:
                        cut_f[i] = min(cut_f[i], cut_f[j] + 1)
        return cut_f[-1]
