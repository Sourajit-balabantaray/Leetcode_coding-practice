class Solution:

    def countCommas(self, n: int) -> int:

        def digits(l):
            cnt = 0

            while l != 0:
                l = l // 10
                cnt += 1

            return cnt

        l = digits(n)

        if l < 4:
            return 0

        else:
            o = 0

            for i in range(1000, n + 1):
                s = digits(i)
                o += (s - 1) // 3

            return o