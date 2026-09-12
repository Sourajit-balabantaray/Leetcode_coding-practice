class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        for i in range(1, len(s)):

            l = s[:i]

            if len(s) % len(l) != 0:
                continue

            q = s.split(l)

            for j in q:
                if j != "":
                    break
            else:
                return True

        return False