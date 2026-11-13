class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # tc = o(n), sc = o(1)
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while (left < right):
            l1 = right - left
            l2 = min(heights[right], heights[left])
            area = l1 * l2
            maxArea = max(maxArea, area)
            if (heights[left] <= heights[right]):
                left += 1
            else:
                right -= 1

        return maxArea
