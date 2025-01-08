digits = "23"

letter_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
result = []
temp_result = ""
for i in digits:

    d = int(i)
    temp_result+=letter_map[d-2]

for i in temp_result:
