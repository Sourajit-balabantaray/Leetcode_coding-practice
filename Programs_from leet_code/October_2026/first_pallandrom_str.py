from typing import List
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def pallan(stri):
            if stri==stri[::-1]:
                return True
            else:
                return False
        for i in words:
            if pallan(i)==True:
                return i
        return ""
        