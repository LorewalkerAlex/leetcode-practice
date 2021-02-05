# https://leetcode-cn.com/problems/get-equal-substrings-within-budget/


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_array = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]

        i = j = max_len = curr_cost = 0
        while j < len(s):
            if curr_cost <= maxCost:
                max_len = max(max_len, j - i)
                curr_cost += cost_array[j]
                j += 1
            else:
                curr_cost -= cost_array[i]
                i += 1
        return max_len if curr_cost > maxCost else max(max_len, j - i)