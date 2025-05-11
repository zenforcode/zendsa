from typing import List

"""

We scan the input string str from left to right while maintaining two indices - headIndex and tailIndex.

At each iteration, we examine a temporary substring [str.charAt(headIndex),str.charAt(headIndex+1),..., str.charAt(tailIndex)] and keep a copy of the shortest valid substring we've seen so far. Said differently, we keep incrementing tailIndex until the above substring contains every unique character in arr.

If the size of the resulting substring equals to arr.length then we return it since by definition there can’t be a shorter valid substring (otherwise, it’ll be missing 1 or more unique characters from arr).

Once we found a valid substring, we increment headIndex as long the substring remains valid. At every increment we also check if the current valid substring is shorter than the previously kept one. If it is, we update result to be the current substring.

We keep repeating the above steps in a loop until we either reach the end of the input string str or return the shortest valid substring, whichever comes first.

To examine the validity of str substrings we use 2 counters:

- uniqueCounter (Integer) - the number of unique characters of arr that our current substring contains.
- countMap (Map/Hash Table) - the number of occurrences of each character of arr in our current substring.

Return Result:
        If a valid window is found, return the smallest substring. If no valid window exists, return "-1".
"""
def get_shortest_unique_substring(arr: List[str], s: str) -> str:
    if not arr or not s:
        return ""

    required_chars = {char: 0 for char in arr}
    unique_chars_needed = len(arr)
    unique_chars_found = 0

    head = 0
    result = ""

    for tail in range(len(s)):
        tail_char = s[tail]

        # If tail_char is part of the required characters
        if tail_char in required_chars:
            if required_chars[tail_char] == 0:
                unique_chars_found += 1
            required_chars[tail_char] += 1

        # Try shrinking the window from the head as long as all unique characters are found
        while unique_chars_found == unique_chars_needed:
            window_len = tail - head + 1
            if window_len == unique_chars_needed:
                return s[head:tail + 1]  # Can't get shorter than this

            if not result or window_len < len(result):
                result = s[head:tail + 1]

            head_char = s[head]
            if head_char in required_chars:
                required_chars[head_char] -= 1
                if required_chars[head_char] == 0:
                    unique_chars_found -= 1

            head += 1

    return result