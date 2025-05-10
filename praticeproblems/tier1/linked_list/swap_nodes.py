from node import Node, create_linked_list, print_linked_list

def swap_nodes(head, left_index, right_index):
    if left_index == right_index:
        return head  

    if left_index > right_index:
        left_index, right_index = right_index, left_index

    prev_one = prev_two = None
    current_one = current_two = None

    current = head
    prev = None
    index = 0

    while current:
        if index == left_index:
            prev_one = prev
            current_one = current
        elif index == right_index:
            prev_two = prev
            current_two = current
            break
        prev = current
        current = current.next
        index += 1

    if not current_one or not current_two:
        return head  # One of the indexes is out of bounds

    if prev_one:
        prev_one.next = current_two
    else:
        head = current_two

    if prev_two != current_one:
        prev_two.next = current_one
    else:
        prev_two = current_two

    # Swap next pointers
    temp = current_one.next
    current_one.next = current_two.next
    current_two.next = temp

    return head

if __name__ == "__main__":
    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 0
    right_index = 6
    head = create_linked_list(arr)
    head = swap_nodes(head, left_index, right_index)
    print_linked_list(head)
