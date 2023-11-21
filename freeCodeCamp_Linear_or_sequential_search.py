# arr = [2, 12, 15, 11, 7, 19, 45]
# Suppose the target element we want to search is  7.

# Approach for Linear or Sequential Search
# Start with index 0 and compare each element with the target
# If the target is found to be equal to the element, return its index
# If the target is not found, return -1


def search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

results = search([2,12,15,11,7,19,45],7)
print(results)


