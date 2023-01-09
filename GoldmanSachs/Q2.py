from ast import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pts = [p1,p2,p3,p4]

        dist = {}

        for i in range(len(pts) - 1):
            for j in range(i+1,len(pts)):
                if(pts[i] == pts[j]):
                    return False
                d = (pts[i][0] - pts[j][0])**2 + (pts[i][1] - pts[j][1])**2
                if d not in dist:
                    dist[d] = 1
                else:
                    dist[d]+=1

        if(len(dist)!=2):
            return False
        diag = side = False
        for i in dist:
            if dist[i] == 4:
                side = True
            elif dist[i] == 2:
                diag = True
            else:
                return False
        if diag and side:
            return True
        