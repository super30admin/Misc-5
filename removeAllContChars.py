# T: O(n), S: O(n)
def removeGroups(s: str) -> str:
    result = []
    i = 0
    n = len(s)

    while i < n:
        count = 1
        # Count consecutive same characters
        while i + count < n and s[i + count] == s[i]:
            count += 1

        if count <= 2:
            # Only keep if count is 1 or 2
            result.extend([s[i]] * count)

        i += count  # Move to next group

    return "".join(result)
