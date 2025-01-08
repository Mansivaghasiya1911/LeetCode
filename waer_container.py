"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

# Mine
height = [1,8,6,2,5,4,8,3,7]
max = 0
for i in range(len(height)):

    for j in range(i+1, len(height)):

        cap = (j - i) * min(height[i], height[j])
        print("Capital : ", cap)
        if cap > max:
            max = cap

left = 0
right = len(height)-1
max_cap = 1

while left < right:

    current_cap = (right - left) * (min(height[right], height[left]))
    max_cap = max_cap if max_cap > current_cap else current_cap
    print(max_cap)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_cap)


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_cap = 0

        while left < right:

            current_cap = (right - left) * (min(height[right], height[left]))
            max_cap = max_cap if max_cap > current_cap else current_cap
            # print(max_cap)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_cap