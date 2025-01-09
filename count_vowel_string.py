"""
2559. Count Vowel Strings in Ranges
Medium
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

"""

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

vowels = set('aeiou')
result = []
vowel_map = {}
ans = 0
for ind in range(len(words)):
    if words[ind][0] in vowels and words[ind][-1] in vowels:
        ans += 1
    vowel_map[ind] = ans

for query in queries:
    vowel_before_start = 0
    if query[0] != 0:
        vowel_before_start = vowel_map[query[0]-1]
    vowel_on_end = vowel_map[query[1]]
    result.append(vowel_on_end - vowel_before_start)

print("Result", result)

