# https://leetcode-cn.com/problems/fair-candy-swap/


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        dif = (sum(A) - sum(B)) // 2
        set_a = set(A)
        for b in B:
            if b + dif in set_a:
                return [b + dif, b]