# we’ll define methods for our LinkedList class that allow us to:
# insert a new head node
# return all the nodes in the list as a string so we can print them out in the terminal!

#   1.  Define an .insert_beginning() method which takes new_value as an argument.
#       Inside the method, instantiate a Node with new_value. Name this new_node.
#       Now, link new_node to the existing head_node.
#       Finally, replace the current head_node with new_node.

#   2.  Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.
#       The method should traverse the list, beginning at the head node, and collect each node’s value in a string.
#       Once the end of the list has been reached, the method should return the string.
#       You can use str() to convert integers to strings!
#       Be sure to add "\n" between values so that each value prints on a new line.

#   3.  Test your code by uncommenting the print statement at the bottom of script.py — did your list print what you expected?

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Part-1 
# Create your LinkedList class below:
class LinkedList:
    def __init__(self,value=None):
        self.head_node = Node(value)

# Part-2
    def get_head_node(self):
        return self.head_node

# Add your insert_beginning and stringify_list methods below:
# Part -1
    def insert_beginning(self,new_value):
        new_node = Node(new_value)
        new_node.set_next_node (self.head_node)
        # since the head_node is being kicked to the next node place, 
        # the head_node is being assigned to the new_node. So now the head node is the new_value
        self.head_node = new_node

# Part -2
    def stringify_list(self):
        string_list=""
        current_node=self.get_head_node()
        while current_node:
            if (current_node.get_value())!= None:
                string_list+=str(current_node.get_value())+ "\n"
            current_node=current_node.get_next_node()
        return string_list

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())