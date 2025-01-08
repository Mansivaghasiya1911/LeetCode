"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""


def twoSum(self, nums, target):
    print(nums, target)

target = 6
num = [3,3]

filtered_list = [i for i in num if i<target]
answer = []
for i in range(0,len(filtered_list)):
    for j in range(i,len(filtered_list)):
        if filtered_list[i] + filtered_list[j] == target:
            answer = [filtered_list[i], filtered_list[j]]

first_index = num.index(answer[0])
second_index = num.index(answer[1])
if first_index == second_index:

    second_index = num.index(answer[1], first_index+1, len(num))

nums = [2,11,7,15]
target = 9
num_map = {}
for i, num in enumerate(nums):

    comple = target - num
    if comple in num_map:
        answer = [num_map[comple], i]
        break
    num_map[num] = i




