class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n:int):
            d=n
            pro=1
            while d!=0:
                x=d%10
                pro*=x
                d=d//10
            return pro
        l=n
        while l>=n:
            s=prod(l)
            if s%t==0:
                return l
            l+=1
        