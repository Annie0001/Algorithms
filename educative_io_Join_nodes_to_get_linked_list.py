# join multiple single nodes containing data using the next pointers,
# and have a single head pointer, pointing to a complete instance of a linked list.

# A single node of singly linked list
class Node:
    # constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
        def __init__(self):
            self.head = None

# Linked list with a single node
LL=LinkedList()
LL.head= Node(3)
print(LL.head.data)

    