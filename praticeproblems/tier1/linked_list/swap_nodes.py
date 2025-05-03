from node import Node, create_linked_list, print_linked_list

def swap_nodes(head, left_index, right_index):
    prev_one, current_one = None, None
    prev_two, current_two = None, None
    current_index = 0
    current = head
    prev = None
    while current:
        if current_index == left_index:
            prev_one = prev
            current_one = current
        if current_index == right_index:
            prev_two = prev
            current_two = current
            break
        prev = current
        current = current.next
        current_index = current_index + 1
        
    if current_two and current_one:
        tmp = current_two.next
        current_two.next = current_one.next
        if prev_one:
            prev_one.next = current_two
        else:
            head = current_two
        prev_two.next = current_one
        current_one.next = tmp
    return head

if __name__=="__main__":
    arr = [3, 4, 5, 2, 6, 1, 9]
    left_index = 0
    right_index = 6
    head = create_linked_list(arr)
    head = swap_nodes(head, left_index, right_index)
    print_linked_list(head)
    print(arr)
    print(left_index)
    print(right_index)