class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great=candies[0]
        for j in candies:
            if j>great:
                great=j
        l=[]
        for i in candies:
            s=i+extraCandies
            if s>=great:
                l.append(True)
            else:
                l.append(False)
        return l

