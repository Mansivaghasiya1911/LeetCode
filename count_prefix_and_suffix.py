words= ["a", "aba", "ababa", "aa"]

result = 0
for i in range(len(words) - 1):

    for j in range(i + 1, len(words)):

        a = len(words[i])

        if words[j][:a] == words[i] and words[j][-a:] == words[i]:
            result += 1