from ast import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = 0
        for key,val in enumerate(nums):
            res += key*val
        tmp = res
        s = sum(nums)

        for i in range(len(nums)-1,-1,-1):
            tmp += s - len(nums)*nums[i]
            res = max(res,tmp)
        return res