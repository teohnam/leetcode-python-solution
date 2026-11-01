"""
Greedy:
Track the minimum price seen so far.
For each price, calculate the potential profit using the minimum
price, then update the maximum profit.
Update the minimum price when a lower price is encountered.

Time: O(n)
"""
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Calculate potential profit if today's price is greater than the minimum price so far.
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price

        return max_profit

"""
Brute force
Time: O(n²)
"""
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(len(prices)):
            if i < len(prices) - 1:
                for j in range(i + 1, len(prices)):
                    max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit

        