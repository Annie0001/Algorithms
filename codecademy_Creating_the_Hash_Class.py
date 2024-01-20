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
    
######  Creating the Compression Function #######
# Hashing functions return a wide range of integers. 
# In order to transform these values into useful indices for our array 
# we need a compression function. A compression function uses 
# modular arithmetic to calculate an array index for a hash map when given a hash code.

#   8-  Create a .compressor() method for your hash map.
#       It should take two parameters: self and hash_code.
#   9-  Take the modulus of the hash code by the map’s array_size in order to 
#       reduce the hash code to a possible index for the array.
#   10- Return the modulus.


    def compressor(self,hash_code):
        return hash_code % self.array_size
    
######  Defining the Setter ###########
# A data structure that is unable to contain data is a sad sight indeed.
# We need to put together all the other steps we’ve taken: plug the key into the hash function, 
# plug the hash code into the compression function, use the array index to find the place in the array, 
# and finally set the value of the array to the value we want.

#   11- Create a .assign() method for the hash map.
#       It should take three parameters: self, key, and value.
#   12- Save the value (just the value for now) to the map’s array 
#       at the index determined by plugging the key into the .hash() method 
#       and plugging the hash code into the .compressor() method.

    def assign(self,key,value):
        #pass
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = value


####### Defining the Getter ######
# There is a natural expectation after placing an item into a bag 
# that we will later be able to remove the item from that bag. Otherwise we have created a hole. 
# Let’s implement retrieval for our hash map.

#  13-  Define a .retrieve()method for HashMap. It should take two parameters: self and key.
#  14-  .retrieve() should calculate the array index in the same way our .assign() does and then retrieve the value at that index.
#  15-  Return that value.

    def retrieve(self, key):
    #pass
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]
