'''
1004 Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

Solution:
1. Brute Force
We start from every index and build all subarrays ending at any point after that. While building the subarray, we count how many zeros are included.
If we are within k zero flips, we update the max length found.
https://youtu.be/4Ul2DCALeOs?t=222
Time: O(N^2), Space: O(1)

2. Sliding Window
We go through the array and if it is 0, we flip it to a 1 and reduce k by 1 (if nums[i] == 0: k--). If we cross the limit of k (i.e., k < 0), we move the left pointer forward to drop a flipped zero (if k < 0 and nums[left] == 0: k++).
We keep track of the maximum window size where we can keep at most k zero flips.
https://youtu.be/4Ul2DCALeOs?t=509
Time: O(N), Space: O(1)
'''
from typing import List

def longestOnes_bruteForce(nums: List[int], k: int) -> int:
    ''' Time: O(N^2), Space: O(1) '''
    if not nums:
        return 0
    N = len(nums)
    max_len = 0,0
    for i in range(N):
        max_flips = k
        j = i
        while max_flips >= 0 and j <= N-1:
            if nums[j] == 0:
                max_flips -= 1
            # there might be a series of consecutive 1s
            # after we have reached the flip limit. Hence
            # we stop when we see flip one more zero (one past the flip limit)
            if max_flips == -1:
                max_len = max(max_len, j - i)
            j += 1
    return max_len


def longestOnes_slidingWindow(nums: List[int], k: int) -> int:
    ''' Time: O(N), Space: O(1) '''
    if not nums:
        return 0
    N = len(nums)
    left,i = 0,0
    max_len, this_len = 0,0
    while i < N:
        if nums[i] == 0:
            k -= 1

        if k == 0:
            this_len = i - left + 1
            max_len = max(max_len, this_len)
        elif k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

        i += 1

    return max_len

def run_longestOnes():
    tests = [([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
             ( [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
    ]
    for test in tests:
        nums, k, ans = test[0], test[1], test[2]
        print(f"\narray = {nums}")
        print(f"k = {k}")
        for method in ['brute-force', 'sliding-window']:
            if method == 'brute-force':
                max_len = longestOnes_bruteForce(nums, k)
            elif method == 'sliding-window':
                max_len = longestOnes_slidingWindow(nums, k)
            print(f"Method {method}: Max no. of consecutive 1's + {k} flips = {max_len}")
            success = (ans == max_len)
            print(f"Pass: {success}")
            if not success:
                print(f"Failed")
                return

run_longestOnes()