class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l=n
        s=0
        q=1
        while n>0:
            i=n%10
            s+=i
            q*=i
            n=n//10
        f=s+q
        if l%f==0:
            return True
        return False

        