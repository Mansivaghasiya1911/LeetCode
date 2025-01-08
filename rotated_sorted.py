# nums = [-100000,100000]
nums = [10,4,-8,7]
valid = 0

l_sum = nums[0]
r_sum = sum(nums[1:])

for ele in range(1, len(nums)):

    if l_sum >= r_sum:
        print("valid")
        valid+=1

    l_sum = l_sum + nums[ele]
    r_sum = r_sum - nums[ele]
    print("LValue: ", nums[ele])
    print("L: ", l_sum)
    print("R: ", r_sum)

