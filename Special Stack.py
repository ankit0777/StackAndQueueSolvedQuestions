# Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if(len(arr)==n):
        return True
    else:
        False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if(len(arr)==0):
        return 1
    else:
        return 0

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    return min(arr)
