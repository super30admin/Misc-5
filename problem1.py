# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

# We maintain a window [left, right] such that the number of 0s in the window is at most k. If the window becomes invalid (i.e., it has more than k zeros), we shrink it from the left until it's valid again.

        left = 0
        ans = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count>k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans