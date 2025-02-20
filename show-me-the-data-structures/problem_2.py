import os
from typing import List
from collections import deque

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    file_list = []
    stack: deque[str] = deque()
    for f in os.listdir(path):
        stack.append(os.path.join(path,f))
    
    while stack:
        current_entry = stack.pop()
        if os.path.isfile(current_entry):
            if current_entry.endswith(suffix):
                file_list.append(current_entry)
        elif os.path.isdir(current_entry):
            files = os.listdir(current_entry)
            for f in files:
                stack.append(os.path.join(current_entry, f))

    return sorted(file_list)
   

if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2
    pass

    # Test Case 3
    pass