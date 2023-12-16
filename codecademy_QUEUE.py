# create a Queue class with an __init__() method. Inside the method:

#   Part - 1
#   set an instance property head equal to None
#   set another instance property tail equal to None

#   Part -  2
#   Below __init__(), define another method peek() 
#   that returns the value of the stack’s head using the Node method get_value().

#   Part -  3
#   Below get_size(), define a new method called has_space().
#   Inside of has_space(), check the value of self.max_size.
#   If self.max_size is None, we will always have space in the queue, so we can return True
#   Otherwise, if there is a value in max_size, return True if max_size is greater than self.get_size()

#   Part -  4
#   Define another method is_empty for Queue. The method should return True if the queue is empty (if the size of the queue is 0).

#   Part - 5
#   Now we’ll make sure we aren’t attempting to peek() on an empty queue. After all, a deli server can’t get an order from a line with no customers!
#   At the top of your peek() method body, use is_empty() to see if the queue is empty.
#   if so, the method should just print “Nothing to see here!”
#   if not, peek() will perform the same as it did before
    
from node import Node
# Create the Queue class below:
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # def peek(self):
    #     return self.head.get_value()

#   Part- 5
    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()
#   Part- 2
# Define get_size() and has_space() below:
    def get_size(self):
        return self.size

#   Part- 3
    def has_space(self):
        if self.max_size == None:
            return True
        if self.max_size > self.get_size():
            return True
        return False
#   Part- 4
    def is_empty(self):
        if self.size == 0:
            return True
        return False
