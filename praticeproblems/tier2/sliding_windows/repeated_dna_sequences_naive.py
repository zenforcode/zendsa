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

"""
Alternative solution:
def findRepeatedDnaSequences(s):
    left = 0
    window_size = 10
    unique_word = set()
    output = set()
    while left + window_size <= len(s):
        current_hash = hash(s[left:left+window_size])
        if current_hash in unique_word:
            current_str = ''.join(s[left:left+window_size])
            if current_str not in output:
                output.add(current_str)
        else:
            unique_word.add(current_hash)
        left+=1        
    return list(output)
"""