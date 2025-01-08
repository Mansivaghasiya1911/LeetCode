nums = [3,4,8,1,7,2,9,5,5]
k = 10

l = 0
r = 1
result = 0
result_array = []
pre_sum = nums[l]
while l<len(nums) and r < len(nums):
    print("L: ", l, r, pre_sum)

    if nums[l] >= k:

        if nums[l] == k :
            result = 1
            break
        else:
            l = l+1
    else:
        pre_sum = pre_sum + nums[r]
        if pre_sum > k:
            pre_sum = pre_sum - nums[l]
            l = l+1
        elif pre_sum == k:
            result_array.append(r-l)
            print("I am here ")
        else:
            r = r+1
        print("pr")