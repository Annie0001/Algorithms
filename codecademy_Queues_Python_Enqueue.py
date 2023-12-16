# “Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue() method.
# There are three scenarios that we are concerned with when adding a node to the queue:
#   1- The queue is empty, so the node we’re adding is both the head and tail of the queue
#   2- The queue has at least one other node, so the added node becomes the new tail
#   3- The queue is full, so the node will not get added because we don’t want queue “overflow”

#   1--Inside the Queue class you built, define a method enqueue() that takes a node value value as a parameter.
#       Add an if clause to check if the queue has space
#       If it does, instantiate a Node that takes value as its argument and assign it to a new variable item_to_add
#       Print “Adding “ + str(item_to_add.get_value()) + “ to the queue!”

from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

# Add your enqueue method below:
def enqueue(self, value):
    if self.has_space():
        item_to_add = Node (value)
        print("Adding " + str(item_to_add.get_value())+" to the queue!")

def peek(self):
    if self.is_empty():
        print("Nothing to see here!")
    else:
        return self.head.get_value()

def get_size(self):
    return self.size

def has_space(self):
    if self.max_size == None:
        return True
    else:
        return self.max_size > self.get_size()

def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("all the fluffy kitties")