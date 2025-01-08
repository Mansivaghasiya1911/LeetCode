nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]


map = {}
result = []
result_set = []
set_nums = list(set(nums))
for i in set_nums:
    count = nums.count(i)
    index = [j for j, val in enumerate(nums) if val == i]
    map[i] = {
        "count": count,
        "index": index
    }

for ind in range(0, len(nums)):

    for ind_j in range(ind+1, len(nums)):
        ind_sum = nums[ind] + nums[ind_j]

        if set([nums[ind], nums[ind_j]]) not in result_set:

            if 0-ind_sum in set_nums:

                if i != ind and i != ind_j:
                    r = [nums[ind], nums[ind_j], 0 - ind_sum]
                    result_set.append(set([nums[ind], nums[ind_j]]))
                    result_set.append(set([nums[ind], 0-ind_sum]))
                    result_set.append(set([nums[ind_j], 0-ind_sum]))
                    result.append(r)
                    break




