'''
1209 Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lowercase English letters.

Solution:
1. Stack
We use a stack to track characters and their frequencies through tuples (char, freq). If a character repeats k times consecutively, we remove them from the stack. We build the result string by unwinding the stacks and then reverse it.
https://youtu.be/4Ul2DCALeOs?t=2171
Time: O(N), Space: O(N)
'''
def removeDuplicates(s: str, k: int) -> str:
    if not s:
        return ""
    stack = []
    for c in s: # O(N)
        # Push char to stack
        if not stack:
            stack.append((c,1)) # push tuple of char and count to stack
        else:
            top = stack[-1][0]
            if c == top:
                # duplicate char, don't push char to stack, only increase it's count
                stack[-1] = (c, stack[-1][1] + 1)
            else:
                # non-duplicate char, push char and count to stack
                stack.append((c,1))

        # remove elements from top if they are duplicates
        while stack and stack[-1][1] == k:
            stack.pop()

    result = ""
    while stack:
        c, count = stack.pop()
        result = result + c*count
    result = result[::-1] # O(N)
    return result

def run_removeDuplicates():
    tests = [("deeedbbcccbdaa", 3, 'aa'),
             ("pbbcggttciiippooaais", 2, 'ps'),
    ]
    for test in tests:
        s, k, ans = test[0], test[1], test[2]
        print(f"\nstring = {s}")
        print(f"k = {k}")
        new_string = removeDuplicates(s, k)
        print(f"new string after removing duplicates = {new_string}")
        success = (ans == new_string)
        print(f"Pass: {success}")
        if not success:
            print(f"Failed")
            return

run_removeDuplicates()
