from LinkedList import LinkedList

# Complete this function:
def nth_last_node(linked_list, n):
  nth_from_last = None
  current = linked_list.head_node
  count = 1

  while(current):
    current = current.next_node
    count = count + 1
    if(count > n):
      if(nth_from_last is None):
        nth_from_last = linked_list.head_node
      else:
        nth_from_last = nth_from_last.next_node

  return nth_from_last


def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)
