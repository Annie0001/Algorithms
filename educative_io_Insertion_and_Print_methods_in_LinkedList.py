# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
# A Linked list class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

# inserting method for the linked list
    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            # after creating the 3rd node, we need this while to push the pointer forward for the 3rd place
            while(current.next):
                # so now the current node would be the node after the head
                current = current.next
            # this helps to put the second node after the head node
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()