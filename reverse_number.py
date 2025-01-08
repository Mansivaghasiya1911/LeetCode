"""
Code
Testcase
Testcase
Test Result
7. Reverse Integer
Solved
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(x.bit_length())

        st = str(x)[::-1]
        print("st:", st)
        if st[-1] == "-":
            st = "-" + st[:-1]

        output = int(st)
        if (output < -(2 ** 31) or output > ((2 ** 31) - 1)):
            output = 0
        return output