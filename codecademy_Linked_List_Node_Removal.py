#   For the purposes of this lesson, we’ll create a function that removes the first node that contains a particular value. 
#   However, you could also build this function to remove nodes by index or remove all nodes that contain a particular value. -->
#   1.  At the bottom of script.py, add a .remove_node() method to LinkedList. It should take value_to_remove as a parameter. 
#       We’ll be looking for a node with this value to remove.
#       In the body of .remove_node(), set a new variable current_node equal to the head_node of the list.
#       We’ll use current_node to keep track of the node we are currently looking at as we traverse the list.

#   2.  Still inside the method body, use an if statement to check whether the list’s head_node has a value that is the same as value_to_remove.
#       If it does, we’ve found the node we’re looking for and we need to adjust the list’s pointer to head_node.
#       Inside the if clause, set self.head_node equal to the second node in the linked list.

# We'll be using our Node class
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

    # Our LinkedList class
    class LinkedList:
        def __init__(self, value=None):
            self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    # Define your remove_node method below:
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.value == value_to_remove:
            self.head_node = current_node.next_node
            return
        previous_node = current_node
        while(current_node):
            if current_node.next_node.value == value_to_remove :
                current_node.set_next_node(current_node.next_node.next_node)
            return
            current_node = current.next_node

