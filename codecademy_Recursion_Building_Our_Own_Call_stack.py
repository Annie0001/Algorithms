# 1.Define a sum_to_one() function that has n as the sole parameter.
# Inside the function body:
# declare the variable result and set it to 1.
# declare the variable call_stack and set it to an empty list.
# Use multiple return to return both of these values: result, call_stack

# 2. Fill in the sum_to_one() function body by writing a while loop after the variable call_stack.
# This loop represents the recursive calls which lead to a base case.
# We’ll want to loop until the input n reaches 1.
# Inside the loop, create a variable execution_context and assign it to a dictionary with the key of "n_value" pointing to n.
# Use a list method to add execution_context to the end of call_stack.
# This is our way of simulating the recursive function calls being “pushed” onto the system’s call stack.
# Decrement n after its value has been stored.
# End the loop by printing call_stack.

def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1: 
        execution_context = {"n_value" : n}
        call_stack.append(execution_context)
        n-=1
        print(call_stack)
    return result, call_stack

sum_to_one(4)