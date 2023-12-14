# create a Queue class with an __init__() method. Inside the method:

#   Part - 1
#   set an instance property head equal to None
#   set another instance property tail equal to None

#   Part -  2
#   Below __init__(), define another method peek() 
#   that returns the value of the stack’s head using the Node method get_value().

from node import Node
# Create the Queue class below:
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.get_value()