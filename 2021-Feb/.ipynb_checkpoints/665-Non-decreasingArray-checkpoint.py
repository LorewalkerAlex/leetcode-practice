# https://leetcode-cn.com/problems/non-decreasing-array/


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        count = 0
        array, count = self.checkArray(nums[:3], count)
        for i in nums[3:]:
            array, count = self.checkArray(array[1:] + [i], count)
            if count > 1:
                return False
        return count <= 1
    
    def checkArray(self, array, count):
        if array[0] <= array[1]:
            if array[1] <= array[2]:
                return array, count
            else:
                if array[0] <= array[2]:
                    array[1] = array[2]
                    return array, count + 1
                else:
                    array[2] = array[1]
                    return array, count + 1
        else:
            if array[1] <= array[2]:
                if array[0] <= array[2]:
                    array[1] = array[0]
                    return array, count + 1
                else:
                    array[0] = array[1]
                    return array, count + 1
            else:
                return array, count + 2