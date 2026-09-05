class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts.sort(reverse=True)
            gifts[0]=int(gifts[0]**0.5)
        return sum(gifts)