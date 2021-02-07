# https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints) - k
        min_sum = curr_sum = sum(cardPoints[:length])
        for i in range(k):
            curr_sum = curr_sum - cardPoints[i] + cardPoints[i+length]
            min_sum = min(min_sum, curr_sum)
        return sum(cardPoints) - min_sum