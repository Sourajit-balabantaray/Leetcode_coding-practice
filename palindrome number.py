class Solution:
    def isPalindrome(self, x: int) -> bool:
        l1=[]
        if x<0:
            return False
        
        while x>0:
            l1.append(x%10)
            x//=10

        if l1[:]==l1[::-1]:
            return True
        else:
            return False      
