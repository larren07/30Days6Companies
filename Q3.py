class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        freq = {}

        for i in secret:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        newGuess = []
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                bulls+=1
                freq[secret[i]]-=1
            else:
                newGuess.append(guess[i])
        
        for i in newGuess:
            if(i in freq and freq[i]>0):
                cows+= 1
                freq[i] -= 1

        res = str(bulls) + "A" + str(cows) + "B"
        return res
