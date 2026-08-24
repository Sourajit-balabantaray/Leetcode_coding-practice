class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort(reverse=True)
            a=stones.pop(0)
            b=stones.pop(0)
            c=a-b
            stones.append(c)
        if stones!=[]:
            return stones[0]
        else:
            return 0
        