from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if not words:
            return True

        counts = Counter()
        for word in words:
            counts.update(word)

        n = len(words)
        for value in counts.values():
            if value % n != 0:
                return False
        return True