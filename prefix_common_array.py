"""
2657. Find the Prefix Common Array of Two Arrays
Medium
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
"""

A = [1,3,2,4]
B = [3,1,2,4]
result = []
map = {}
common_count = 0
for i in range(0, len(A)):
    if map.get(A[i], 0) == 0:
        map[A[i]] = 1
    else:
        common_count +=1
    if map.get(B[i], 0) == 0:
        map[B[i]] = 1
    else:
        common_count +=1

    result.append(common_count)



