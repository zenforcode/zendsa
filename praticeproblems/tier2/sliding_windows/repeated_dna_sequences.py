from typing import List
def findRepeatedDnaSequences(s: str) -> List[str]:
    if len(s) < 10:
        return []
    sequence_map = {}
    output = set()
    left = 0
    window_size = 10
    while left + window_size <= len(s):
        substring = s[left:left + window_size]
        count = sequence_map.get(substring, 0)
        sequence_map[substring] = count + 1
        if count + 1 == 2:  # Only add the second time it's seen
            output.add(substring)
        left += 1
    return list(output)
