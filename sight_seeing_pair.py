"""
1014. Best Sightseeing Pair
Medium
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
"""

values = [2,2,1]

i_list = []
j_list = []
max_value = 0

for k in range(len(values)):
    i_list.append(values[k] + k)
    j_list.append(values[k] - k)

while max_value == 0 :
    print(i_list)
    max_i_element = max(i_list)
    index_max_element = i_list.index(max_i_element)

    if (j_list[index_max_element +1:]):
        print("here", j_list[index_max_element +1:])
        max_j_element = max(j_list[index_max_element +1:])
        max_value = max_i_element + max_j_element
        break
    else:
        i_list[index_max_element] = 0



