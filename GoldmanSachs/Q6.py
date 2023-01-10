from ast import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.res = None
        self.sc = 0
        
        def rec(arrows, i, sc):
            if(i < 0 ):
                if(sc> self.sc):
                    self.res = curr.copy()
                    self.sc = sc
                return 
            
            #not pick
            rec(arrows,i-1, sc)

            #pick
            if(arrows > aliceArrows[i]):
                curr[i] = aliceArrows[i] + 1
                rec(arrows - aliceArrows[i] - 1, i-1, sc + i )
                curr[i] = 0
            return 
        
        curr = [0]*12
        maxScore = 0
        rec(numArrows, 11, 0)
        self.res[0] += numArrows - sum(self.res)
        return self.res
        