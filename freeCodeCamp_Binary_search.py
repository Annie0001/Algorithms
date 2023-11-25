# def binary_search(nums,target):
#     # find the middle value
#     mid_index = int(len(nums)/2)
#     middle_value = nums[mid_index]
#     # compare the target element with the middle element of the array
#     if target == middle_value:
#         return mid_index
#     if target < middle_value:
#         for i in range(mid_index):
#             if nums[i] == target:
#                 return i
#     else:
#         for i in range(mid_index, len(nums)):
#             if nums[i] == target:
#                 return i
#     return -1

# result= binary_search([2,12,15,17,27,29,45], 17)
# print(result)

# result= binary_search([2,12,15,17,27,29,45], 12)
# print(result)

# result= binary_search([2,12,15,17,27,29,45], 120)
# print(result)
# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------
# ///////////  Binary Search /////////////////
# arr = [2, 12, 15, 17, 27, 29, 45]
# target = 17

# Approach for Binary Search
# Compare the target element with the middle element of the array.
# If the target element is greater than the middle element, then the search continues in the right half.
# Else if the target element is less than the middle value, the search continues in the left half.
# This process is repeated until the middle element is equal to the target element, or the target element is not in the array
# If the target element is found, its index is returned, else -1 is returned.


def binary_search(nums,target):
    start=0
    end = len(nums)-1

    while start<=end:
        mid = start + (end-start)//2
        if nums[mid]>target:
            end=mid-1
        elif nums[mid]<target:
            start=mid+1
        else:
            return mid
    return -1

result=binary_search([2, 12, 15, 17, 27, 29, 45],17)
print(result)

result=binary_search([2, 12, 15, 17, 27, 29, 45],12)
print(result)

result=binary_search([2, 12, 15, 17, 27, 29, 45],45)
print(result)

result=binary_search([2, 12, 15, 17, 27, 29, 45],30)
print(result)
