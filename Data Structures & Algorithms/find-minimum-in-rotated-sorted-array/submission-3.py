# need to revisit
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # TC: O(log n), SC: O(1)
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # If middle element is greater than rightmost element,
            # the minimum element must be in the right half.
            if nums[m] > nums[r]:
                l = m + 1
            else:
                # Minimum element is at m or to the left of m.
                r = m

        return nums[l]