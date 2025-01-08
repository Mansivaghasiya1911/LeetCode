"""Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            longest = ""
            longest_list = []
            for i in s:

                if i not in longest:
                    longest+=i
                else:
                    ind = longest.index(i)
                    longest_list.append(longest)
                    longest = longest[ind+1:]
                    longest += i
            longest_list.append(longest)
            if len(longest_list) !=0:
                res = max(longest_list, key = len)
                output = len(res)
                return output
            else:
                return 1
        else:
            return 0