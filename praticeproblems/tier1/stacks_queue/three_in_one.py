### describe a single array to implement three stacks.

# we can assume that each stack at max 1000 items then we see if we can remove  the assumtion
[]
# top_1, bottom_1, max_pos_1, top_2, bottom_2,max_pos_2 ,top_3, bottom_3, max_pos_3

#1..1000 first stack
#1000..2000 second stack
#2000..3000 third stack.
#when a stack increase of more than max elements we double the size and move to the end, copying all the stacks and updating the pointers
# we need to know on which stack with pop and push
import copy
from typing import Final
DEFAULT_SIZE: Final[int] = 100
# how do we set in python the generic type
class StackException(Exception):
    ...

class ThreeStack:
    def __init__(self):
        self._stack_dict: dict[int, list[int,int]] = {1: [0,0], 2: [DEFAULT_SIZE,0], 3: [DEFAULT_SIZE*2,0]}
        self.data_array = [0] * DEFAULT_SIZE * 3
    
    def push(self, stack_index: int, data: any):
        if stack_index not in self._stack_dict.keys():
            raise ValueError(f"Invalid stack value {stack_index}")
        bottom, top = self._stack_dict[stack_index]
        top = top + 1
        if top >= DEFAULT_SIZE:
            # we need to copy
            temporary_array = [0] * (len(self.data_array) + (top-bottom))
            for index, value in self._stack_dict.items():
                bottom, top = value
                if index > 
        self.data_array[top] = data


    def pop(self, stack_index: int) -> any:
        if stack_index not in self._stack_dict.keys():
            raise ValueError(f"Invalid stack value {stack_index}")
        bottom, top = self._stack_dict[stack_index]
        if bottom == top:
            raise StackException("Out of stack value")
        else:
            bottom = self._stack_dict[stack_index][0]
            top = self._stack_dict[stack_index[1]]
            self._stack_dict[stack_index[1]] = self._stack_dict[stack_index[1]] - 1
            return self.data_array[top]