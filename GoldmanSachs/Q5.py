from ast import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = {}
        res = 1000000
        for key,val in enumerate(cards):
            if val not in freq:
                freq[val] = [key]
            else:
                res = min(res,key - freq[val][-1] + 1)
                # print(freq[val])
                freq[val].append(key)
        if(res == 1000000):
            return -1
        return res