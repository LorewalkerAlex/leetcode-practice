# https://leetcode-cn.com/problems/longest-turbulent-subarray/


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = max_len = flag = 0
        for j in range(len(arr)):
            if j == i:
                max_len = max(max_len, 1)
            elif j - i == 1:
                if arr[i] == arr[j]:
                    i = j
                else:
                    if arr[j] < arr[i]:
                        flag = 1
                    max_len = max(max_len, 2)
            else:
                if flag:
                    if arr[j-1] < arr[j]:
                        flag = 0
                        max_len = max(max_len, j - i + 1)
                    elif arr[j-1] == arr[j]:
                        flag = 0
                        i = j
                    else:
                        flag = 1
                        i = j - 1
                        max_len = max(max_len, 2)
                else:
                    if arr[j-1] > arr[j]:
                        flag = 1
                        max_len = max(max_len, j - i + 1)
                    elif arr[j-1] == arr[j]:
                        i = j
                    else:
                        i = j - 1
                        max_len = max(max_len , 2)
        return max_len