"""
6. Zigzag Conversion
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""

s = "PAYPALISHIRING"
numRows = 3


result = ""
s_len = len(s)
if len(s) == numRows or numRows == 1:
    result = s
else:
    result_list = [""]*numRows
    map = list(range(0, numRows))
    while len(map) < s_len:
        map.extend(map[::-1][1:])
    for i in range(s_len):
        result_list[map[i]] += s[i]

    result = "".join(result_list)

