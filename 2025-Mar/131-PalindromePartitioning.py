# https://leetcode.cn/problems/palindrome-partitioning/description/


from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        else:
            res = []
            for i in range(1, len(s)+1):
                if self.is_palindrome(s[:i]):
                    if not s[i:]:
                        res.append([s])
                    else:
                        for l in self.partition(s[i:]):
                            res.append([s[:i]] + l)

            return res
    

    def is_palindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        else:
            if s[0] == s[-1]:
                return self.is_palindrome(s[1:-1])
            else:
                return False