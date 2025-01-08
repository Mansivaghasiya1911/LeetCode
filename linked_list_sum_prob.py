"""
Code


Testcase
Testcase
Test Result
2. Add Two Numbers
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

l1 = [2,4,3]
l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

ll1 = "".join([str(i) for i in l1[::-1]])
ll2 = "".join([str(i) for i in l2[::-1]])

sum = str(int(ll2) + int(ll1))[::-1]
answer = [int(i) for i in sum]
print(answer)
print(sum)