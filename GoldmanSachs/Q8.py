from ast import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ct = {}
        res = 0

        for i in nums:
            rev = int(str(i)[::-1])
            
            diff = i - rev
            if diff in ct:
                res = (res + ct[diff])%(10**9 + 7)
                ct[diff]+=1
            else:
                ct[diff] = 1
        
        return res