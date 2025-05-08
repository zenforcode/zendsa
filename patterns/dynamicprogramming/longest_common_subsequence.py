from typing import List

def diff_between_two_strings(source: str, target: str) -> List[str]:
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if source[i] == target[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # Backtrack to build the diff
    output = []
    i, j = m, n
    while i > 0 and j > 0:
        if source[i-1] == target[j-1]:
            output.append(source[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            output.append("-" + source[i-1])
            i -= 1
        else:
            output.append("+" + target[j-1])
            j -= 1
            
    while i > 0:
        output.append("-" + source[i-1])
        i -= 1
    while j > 0:
        output.append("+" + target[j-1])
        j -= 1

    return output[::-1]

