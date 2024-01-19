#   In Python we don’t have an array data structure that uses a contiguous block of memory. 
#   We are going to simulate an array by creating a list and keeping track of the size of the list
#   with an additional integer variable. This will allow us to design something that resembles a hash map. 

#   1- Create a class called HashMap.
#   2- Give HashMap a constructor which takes both self and array_size as parameters.
#      .array_size should be assigned to an instance variable of the same name (.array_size), and represents the size of the array.
#   3- Create an instance variable called .array, which is a list of size array_size. Make each element of .array equal to None.

class HashMap:
    def __init__(self,array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

###### Creating the Hashing Function ########
#   4-  Create a method for HashMap called .hash(). This method should take two arguments: self and key.
#   5-  Turn the key into a list of bytes by calling key.encode(). Save this into a variable called key_bytes.
#   .encode() is a string method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.
#   6-  Turn the bytes object into a hash code by calling sum() on key_bytes. Save the result from that into a variable called hash_code.
#   7-  Return hash_code.

    def hash(self,key):
        # pass
        key_bytes = key.encode()
        # hash_code = key_bytes.sum()
        hash_code = sum(key_bytes)
        return hash_code