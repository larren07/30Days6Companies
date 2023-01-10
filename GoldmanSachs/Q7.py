class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*(n+forget)
        dp[0] = 1
        for i in range(n):
            for j in range(i+delay,i+forget):
                dp[j]= (dp[j] + dp[i])%1000000007
        
        res = 0
        i = 0
        while(forget):
            res = (res + dp[n-i-1])%1000000007
            forget -=1
            i+=1

        return res