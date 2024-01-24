# In Python, a recursive function accepts an argument and includes a condition to check whether it matches the base case. 
# A recursive function has:
# Base Case - a condition that evaluates the current input to stop the recursion from continuing.
# Recursive Step - one or more calls to the recursive function to bring the input closer to the base case.

def countdown(value):
    if value <= 0:   #base case  
        print("done")
    else:
        print(value)
        countdown(value-1)  #recursive case 

countdown(20)