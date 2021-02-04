# https://leetcode-cn.com/problems/longest-repeating-character-replacement/submissions/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {letter:i for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        counts = [0] * 26
        max_len, left, right = 0, 0, 0
        while right < len(s):
            counts[d[s[right]]] += 1
            right += 1
            while sum(counts) - max(counts) > k:
                counts[d[s[left]]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
    
    def betterone(self, s, k):
        d, res, start = {}, 0, 0
        for i, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            if i - start + 1 - d[max(d, key=d.get)] > k:
                d[s[start]] -= 1
                start += 1
            else:
                res = max(res, i - start + 1)
        return res