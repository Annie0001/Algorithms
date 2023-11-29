# we make a Node class that holds some data and a single pointer next,
# that will be used to point to the next Node type object in the Linked List.
class Node:
    #Constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

first = Node(3)
print(first.data)
