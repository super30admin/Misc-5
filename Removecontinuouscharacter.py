# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c,1])
        res = ""
        for el in stack:
            res += el[0] * el[1]
        return res