class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_width = 0
        num_zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            width = r-l+1
            max_width = max(max_width,width)
        return max_width
