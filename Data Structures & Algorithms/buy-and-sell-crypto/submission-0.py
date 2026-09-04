class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost=prices[0]
        max_profit=float('-inf')

        n=len(prices)
        for i in range(n):
            if mincost>prices[i]:
                mincost=prices[i]
            profit=prices[i]-mincost

            if profit>max_profit:
                max_profit=profit
        return max_profit
        