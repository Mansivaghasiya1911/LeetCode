"""
1400. Construct K Palindrome Strings
Medium
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
s = "leetcode", k = 3
s = "true", k = 4
"""

s = "eminem"
k = 2

# Solution
import math
s_len = len(s)
s_multiple = 0
result = False
for i in set(s):
    s_multiple += math.floor(s.count(i)/2)
if k == 1:
    necesary_duplicate = math.floor(s_len / 2)
else:
    necesary_duplicate = math.floor(s_len/k)

if s_len/k == 1:
    result = True
elif necesary_duplicate ==0:
    result = False
else:
    if s_multiple >= necesary_duplicate:
        result = True
    else:
        result = False

print(result)




if len(s) == k:
    result = True
if len(s) < k:
    result = False
odd = 0
for char in set(s):
    if s.count(char) % 2:
        print(s.count(char) % 2)
        odd += 1
if odd > k:
    result = False