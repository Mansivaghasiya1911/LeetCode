nums = [4,3,1,6]
queries = [[0,2],[2,3]]

result = []
parity_array = [1]*len(nums)
false_range = []

for index, ele in enumerate(nums):
    # even : 0 Odd 1
    if ele % 2==0:
        parity_array[index] = 0

for ind in range(1, len(nums)):
    if parity_array[ind] == parity_array[ind-1]:
        false_range.append([ind-1,ind])


for query in queries:

    r = True
    start = query[0]
    end = query[1]

    for false_pair in false_range:

        if false_pair[0] >= start and false_pair[1] <= end:
            r = False

    result.append(r)