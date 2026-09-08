class Solution:
    def countCommas(self, n: int) -> int:
        def digits(l):
            cnt=0
            while l!=0:
                l=l//10
                cnt+=1
            return cnt
        l=digits(n)
        if l<4:
            return 0
        else:
            return n-999
        