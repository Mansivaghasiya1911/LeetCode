"""
137. Single Number II
Medium
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

nums = [0,1,0,1,0,1,99]

mapping = []
wrong = []

for i in nums:

    if i in mapping:
        wrong.append(i)
        mapping.remove(i)
    elif i not in wrong:
        mapping.append(i)

result = mapping[0]
