
## Reasoning Behind Decisions:

The OrderedDict from the collections module is used in this implementation of an LRU (Least Recently Used) Cache because it maintains the order of elements based on insertion. This property allows us to efficiently track which items were least recently used and remove them when necessary. 
- That collection class provide a method move_to_end() that it can use to maintain the least recently used property. So we can use 
  each time we do a get. In that case we change the order putting the recently used to the bottom. When we extract an item, with 
  popitem we get the the last inserted (top) in the OrderedDictionary but since the we've used move_to_end, at the top there will
  be the least recently used in case of eviction. We do the popitem only when we reach the max capacity.

## Time Efficiency:
-  get() -> O(1) + move_to_end(), that's also O(1)
-  set() -> O(1) + popitem(), also it is O(1)
-  popitem() -> O(1)

## Space Efficiency:
 - O(n) + extra double linked list pointers needed to track the order in OrderedDict. In the double linked list keep track of the order of the hash/key insertion in the dictionary
