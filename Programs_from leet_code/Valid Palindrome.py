class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=""
        for i in s:
            if i.isalnum():
                j+=i.lower()
        left=0
        right=len(j)-1
        while left < right:
            if j[left]!=j[right]:
                return False
            left+=1
            right-=1
        return True
