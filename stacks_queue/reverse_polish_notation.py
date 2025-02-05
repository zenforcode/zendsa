from stack_list import Stack
def evaluate_post_fix(input_list: list) -> int:
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()
    n = None
    for item in input_list:
        if item == "+":
            n = stack.pop()
            n+=stack.pop()
            stack.push(n)
        elif item == "*":
            n = stack.pop()
            n*=stack.pop()
            stack.push(n)
        elif item == "/":
            n = int(stack.pop())
            n = int(stack.pop()/n)
            stack.push(n)
        elif item == "-":
            n = stack.pop()
            n= int(stack.pop()/n)
            stack.push(n)
        else:
            n = int(item)
            stack.push(n)
    return stack.pop()

if __name__=="__main__":
    postfix = ["4", "13", "5", "/", "+"]
    if evaluate_post_fix(postfix) == 6:
        print("Success!")