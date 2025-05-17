from typing import List

def get_shortest_unique_substring(arr: List[str], s: str) -> str:
    """
    Finds the shortest substring of `s` that contains all unique characters from `arr`.
    We scan the input string `s` from left to right while maintaining two indices: `head` and `tail`.
    At each iteration, we examine a temporary substring `s[head:tail+1]` and keep track of the shortest valid
    substring encountered so far. We increment `tail` until the substring contains all unique characters in `arr`.
    If the current substring has the same length as `arr`, we return it immediately, as it's the shortest possible
    valid substring.
    Once we find a valid substring, we increment `head` to shrink the window while it remains valid. If a shorter valid
    substring is found during this process, we update the result.
    We use the following data structures to check substring validity:
    - `required_chars` (dict): tracks the frequency of characters from `arr` in the current window.
    - `unique_chars_found` (int): counts how many unique required characters are present in the window.

    Args:
        arr (List[str]): List of required unique characters.
        s (str): Input string.

    Returns:
        str: The shortest valid substring containing all characters in `arr`, or "-1" if none exists.
    """
    if not arr or not s:
        return "-1"

    required_chars = {char: 0 for char in arr}
    unique_chars_needed = len(arr)
    unique_chars_found = 0

    head = 0
    result = ""

    for tail in range(len(s)):
        tail_char = s[tail]

        if tail_char in required_chars:
            if required_chars[tail_char] == 0:
                unique_chars_found += 1
            required_chars[tail_char] += 1

        # Shrink the window from the head while the substring remains valid
        while unique_chars_found == unique_chars_needed:
            window_len = tail - head + 1
            if window_len == unique_chars_needed:
                return s[head:tail + 1]  # Shortest possible, return immediately

            if not result or window_len < len(result):
                result = s[head:tail + 1]

            head_char = s[head]
            if head_char in required_chars:
                required_chars[head_char] -= 1
                if required_chars[head_char] == 0:
                    unique_chars_found -= 1

            head += 1

    return result if result else "-1"
