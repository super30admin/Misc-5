# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zcount = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zcount += 1

            if zcount > k:
                l += 1
                if nums[l-1] == 0:
                    zcount -= 1

            if zcount <= k:
                res = max(res, r-l+1)

        return res