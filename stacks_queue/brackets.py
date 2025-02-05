from stack_array import Stack

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    s = Stack()
    for c in equation:
        if c == '(':
            s.push(s)
        elif c == ')':
            data = s.pop()
            if data is None:
                return False
    if s.size() == 0:
        return True
    else:
        return False