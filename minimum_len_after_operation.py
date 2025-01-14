"""
3223. Minimum Length of String After Operations
Medium

You are given a string s.

You can perform the following process on s any number of times:

Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
Delete the closest character to the left of index i that is equal to s[i].
Delete the closest character to the right of index i that is equal to s[i].
Return the minimum length of the final string s that you can achieve.
"""

""" 
Beats 75% solutions
Intution :
if a appearce for 3 times we can remove 2 from that 
if a appearce for 4 times we can remove 2 as only 2 will satisfy condition of having same character on right and left side 

all odd numbers behaves as 3 and all even number behaves as 4 
so for example if occurance is 9 than we can remove 8 out of that 

"""

s = "abaacbcbb"

result = len(s)
for i in set(s):
    c = s.count(i)
    if c >= 3:
        result -= c-1
        if c%2 ==0:
            result -= -1

print(result)




