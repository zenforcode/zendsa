
## Reasoning Behind Decisions:

## Time Efficiency:
We've two cases
N - number of the groups including subgroup.
M - number of the groups excluding subgroups.
K - number of users spread out between groups.

### Best case scenarios
1. The user is in the first group O(1) 
2. The user is at upper level groups O(M).
### Worst case scenario
We have to visit the tree for finding the subgroup that the user belong. 
So we have to check in the worst scenario all nodes in the tree. And for each
node we've to check in all users. Since we keep the users in a list O(N*K),
but if it it were implemented as set we should just O(N).
## Space Efficiency:
O(N+K) for the tree and the list of users.
