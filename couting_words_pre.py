"""
2185. Counting Words With a Given Prefix
Easy
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
"""

words = ["leetcode","win","loops","success"]
pref = "code"
# pref = "at"
ans = 0
prefix_len = len(pref)
for i in words:

    if pref == i[:prefix_len]:
        ans +=1