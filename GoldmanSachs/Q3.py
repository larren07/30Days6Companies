class Solution:
    def trailingZeroes(self, n: int) -> int:
        i,c = 5,0
        
        while(i<=n):
            c+=n//i
            i*=5
        return c