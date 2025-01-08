words = ["leetcoder","leetcode","od","hamlet","am"]

result = []
lst2 = sorted(words, key=len)

for i in range(len(words)):

    for j in range(i+1, len(words)):

        print(lst2[i], lst2[j])
        if lst2[i] in lst2[j] :

            result.append(lst2[i])

    result