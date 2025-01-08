s = "aabca"

answer = 0
letters = set(s)

for letter in letters:

    i, j = s.index(letter), s.rindex(letter)
    letter_set = set()
    for k in s[i+1: j]:

        letter_set.add(k)
    answer += len(letter_set)

print(answer)
