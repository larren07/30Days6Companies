from ast import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(len(points)):
            dict={}
            for j in range(len(points)):
                if(i == j):
                    continue
                d = (points[i][1] - points[j][1])**2 + (points[i][0] - points[j][0])**2
                if d not in dict:
                    dict[d] = 1
                else:
                    dict[d]+=1
            
            for val in dict:
                res+= dict[val]*(dict[val]-1)
        return res