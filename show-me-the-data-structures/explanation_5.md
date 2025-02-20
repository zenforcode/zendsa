
## Reasoning Behind Decisions:
This implementation provides a basic blockchain structure using a linked list of blocks, each containing timestamped data and a SHA-256 hash for integrity. The linked list is not really a linked list but a list of blocks. We proof the insertion to the list
of blocks, adding the previous block hash the last ones thru list direct access.
## Time Efficiency:
In CPython a list data type is implemented as dynamic array. CPython uses a contiguous block of memory (like C arrays).
Each element in the list is a pointer to an actual Python object. So the complexity:
- insertion O(N)
- appending O(1)
- traversing O(N)
- access thru index O(1)
In our case we append and access to the list and we print all the list so it is O(N), where N is the number of blocks

## Space Efficiency:
- O(N), where the N is the number of blocks.
