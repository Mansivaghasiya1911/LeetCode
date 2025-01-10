"""
983. Minimum Cost For Tickets
Medium
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
"""

days = [1,4,6,7,8,20]
costs = [2,7,15]

max_cost = costs[0] * len(days)

difference_list = []
for i in range(len(days)-1):
    difference_list.append(days[i+1]-days[i])
sum(difference_list)+1