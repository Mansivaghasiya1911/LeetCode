"""
8. String to Integer (atoi)
Medium
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""

s = "     +004500"

s = s.lstrip()
if not s.isnumeric():
    limit = 2**31
    result = ""

    zero_flag = 0
    any_digit = 0
    for ind, i in enumerate(s):
        print(i)

        if not (result+ s[ind:]).isnumeric():
            if i.isnumeric():

                if i != "0" or any_digit!= 0:
                    result+= i
                    any_digit = 1

                else:
                    zero_flag = 1
            else:
                if i == '-' or i == "+":
                    if ind ==0:
                        result += i
                    else:
                        break
                else:
                    break
        else:
            result = result + s[ind:]

    if result == "" or any_digit == 0:
        result = 0
    else:
        result = int(result)
else:
    result = int(s)
if  result < -limit:
    result = -limit
elif result > limit -1:
    result = limit -1