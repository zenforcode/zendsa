## Difference Between Two Strings
### Problem
Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source to target that uses the least edits possible.
For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"
More formally, for each character C in source, we will either write the token C, which does not count as an edit; or write the token -C, which counts as an edit.
Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.
At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, the letters should spell out target (when ignoring plus-signs.)
In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), and ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.
If there are multiple answers, use the answer that favors removing from the source last.

### Note
When it comes to this text usually think that it is a two pointers problem but a diff is never like a two pointers problems so don't came up
with:

```

if ord(source[i]) == ord(target[j]):
    output.append(source[i])
    i += 1
    j += 1
elif ord(source[i]) < ord(target[j]):
    output.append("-" + source[i])
    i += 1
else:
    output.append("+" + target[j])
    j += 1
```

This compares characters based on ASCII values and decides to:

1. Match if equal,
2. Delete from source if it's "less than" target (ASCII-wise),
3. Insert from target if source is "greater than" target.


This fails and why:
1. It assumes character ordering implies structural alignment.
This is not true. Just because 'C' < 'D' in ASCII doesn't mean 'C' in source should be deleted in favor of 'D' in target.

Example:
```
source = "ABCD"
target = "ABDF"

Your logic:

    Sees 'C' < 'D' → deletes 'C'

    Sees 'D' == 'D' → matches

    Continues...
```
But suppose the target string had reordered or repeated characters? Your ASCII comparison wouldn't find the best matching sequence.

2. It doesn’t handle substitutions properly.
If the characters differ, and there's a substitution (like 'X' replaced by 'Z'), your greedy method treats them as separate delete and insert operations based only on ASCII value—not their actual position in structure.

Real diff should consider:

- Is it better to match later?
- Is it better to skip one to get a longer match?
  
This requires backtracking and dynamic programming.

3. No global view.

You only look at source[i] and target[j], but never "look ahead" to consider better matches later. This local view causes:
1. Skipped potential matches
2. Redundant deletions/insertions

### What You Need Instead:

A good diff algorithm must:

1. Track character positions regardless of ASCII order
2. Align characters based on longest common subsequence
3. Backtrack to construct the best path

That’s what dynamic programming (DP) provides as we see in [Solution](./longest_common_subsequence.py)

