from LinkedList import LinkedList

# Complete this function:
def find_middle(linked_list):
  fast = linked_list.head_node
  slow = linked_list.head_node
  while fast is not None:
    fast = fast.next_node
    if fast is not None:
      fast = fast.next_node
      slow = slow.next_node
  return slow

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
