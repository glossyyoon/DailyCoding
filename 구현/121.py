import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = sys.maxsize
        maxx = -sys.maxsize
        for i in prices:
            minn = min(i, minn)
            maxx = max(i - minn, maxx)
        return maxx
