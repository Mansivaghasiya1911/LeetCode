nums = [0,0,1,1,1,2,2,3,3,4]

result = []
k = 0
for i in nums:
    if i not in result:
        result.append(i)
        k+=1

k = 1
j = nums[0]
for i in nums[1:]:
    if j!=i:
        j = i
        k +=1
    else:
        nums.remove(i)
