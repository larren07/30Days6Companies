from ast import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def rec(i,tmp,n):

            if(len(tmp) == k):
                if(n == 0):
                    res.append(tmp.copy())
                return
            
            for j in range(i,10):
                tmp.append(j)
                rec(j+1,tmp,n-j)
                tmp.pop(-1)

        rec(1,[],n)
        return res
            