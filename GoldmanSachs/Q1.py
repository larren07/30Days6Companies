from ast import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        freq = {}
        res = 0
        for i in range(len(points)-1):
            curr = 0
            for j in range(i+1, len(points)):
                if((points[j][0] - points[i][0]) == 0):
                    slope = float('inf')
                else:
                    slope = (points[j][1] - points[i][1])/ (points[j][0] - points[i][0])

                if slope in freq:
                    freq[slope]+=1
                else:
                    freq[slope] = 1

                curr = max(curr,freq[slope])

            res = max(res,curr)
            freq={}

        return res +1