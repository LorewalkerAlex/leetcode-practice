# https://leetcode-cn.com/problems/sliding-window-median/


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        screen = sorted(nums[:k])
        res = [self.get_mudium(screen)]
        for i in range(len(nums) - k):
            screen.pop(self.binary_search(screen, nums[i]))
            insert_idx = self.binary_search(screen, nums[i+k])
            if screen and screen[insert_idx] < nums[i+k]:
                screen.insert(insert_idx+1, nums[i+k])
            else:
                screen.insert(insert_idx, nums[i+k])
            res.append(self.get_mudium(screen))
        return res


    def get_mudium(self, lst):
        length = len(lst)
        if length % 2 == 0:
            return (lst[length // 2 - 1] + lst[length // 2]) / 2
        else:
            return lst[(length - 1) // 2]

    def binary_search(self, lst, val):
        if len(lst) <= 1:
            return 0
        middle = len(lst) // 2
        if val == lst[middle]:
            return middle
        elif val < lst[middle]:
            return self.binary_search(lst[:middle], val)
        else:
            return middle + self.binary_search(lst[middle:], val)
        
