"""
916. Word Subsets
Medium
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
"""
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]

mapping = {}
result = []
word2_mapping = {}

for ind, chr in enumerate(words1):

    for i in chr:
        # print(i)
        mapping[ind] = mapping.get(ind, {})
        mapping[ind][i] = mapping.get(ind).get(i, 0) + 1

for word in words2:

    word2_mapping[word] = word2_mapping.get(word, {})

    for j in set(word):
        word2_mapping[word][j] = word.count(j)

for ind in range(len(words1)):
    flag = 1
    for word_ele in word2_mapping.keys():
        mapping_2 = dict(mapping)
        print("Maping: ", mapping_2)
        for word in word_ele:
            # print("word:" , word, mapping[ind].get(word, 0))
            if mapping_2[ind].get(word, 0) >= 1:
                mapping_2[ind][word] -= 1
            else:
                flag = 0
                break
    if flag == 1:
        result.append(words1[ind])


















